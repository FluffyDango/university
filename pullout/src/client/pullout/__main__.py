# Some imports are done in functions to reduce startup time
import click
from .backend import SQLiteDb
from . import printer
from .carddav import DavConnection
from . import enable_debug, DEBUG

# Make sure that if images are provided, only addressbook option is available
def validate_images_option(ctx, param, value):
    image_options = ['print_all', 'print_vcards', 'print_addressbooks', 'del_addressbook', 'export', 
                     'add_interactively', 'remove', 'modify_id', 'name', 'tel', 'email', 'org']

    if value and any(ctx.params.get(option) for option in image_options):
        raise click.UsageError('If images are provided, only addressbook option is available.')
    return value


# Make -h and --help the same
@click.command(context_settings=dict(help_option_names=['-h', '--help']))
# You either provide image list or search options or nothing to output all vcards
@click.argument('images', nargs=-1, required=False, type=click.Path(exists=True, dir_okay=False, resolve_path=True), callback=validate_images_option)
@click.option('-p', '--print', 'print_all', is_flag=True, help='Print all contacts with their addressbooks')
@click.option('-pc', '--print-contacts', 'print_vcards', is_flag=True, help='Print all vcards of current addressbook')
@click.option('-pa', '--print-addressbooks', 'print_addressbooks', is_flag=True, help='Print all addressbooks')
@click.option('-a', '--addressbook', type=str, help='Change to addressbook')
@click.option('-ca', '--create-addressbook', 'create_addr', type=str, help='Create addressbook')
@click.option('-da','--del-addressbook', 'del_addressbook', type=str, help='Delete addressbook')
@click.option('-e', '--export', type=click.Path(resolve_path=True), help='Output data to PDF file')
@click.option('-i', '--add-interactively', is_flag=True, default=False, help='Add contact interactively')
@click.option('-r', '--remove', type=int, help='Remove contact by specifying its ID')
@click.option('-m', '--modify', 'modify_id', type=int, help='Modify contact by specifying its ID')
@click.option('-s', '--sync', is_flag=True, default=False, help='Sync with CardDav server')
@click.option('--debug', is_flag=True, default=False, help='Debug mode')
@click.option('--reset', is_flag=True, default=False, help='Reset database')
@click.option('--init', type=str, help='Specify CardDav server URL')
@click.option('--name', type=str, help='Search by name')
@click.option('--tel', type=str, help='Search by telephone number')
@click.option('--email', type=str, help='Search by email')
@click.option('--org', type=str, help='Search by organization')
def main(images: list, print_all: bool, print_vcards: bool, print_addressbooks: bool,
         addressbook: str, create_addr: str, del_addressbook: str, export: str, sync: bool, debug: bool,
         modify_id: int, add_interactively: bool, remove: int, reset: bool, init: str,
         name: str, tel: str, email: str, org: str) -> None:
    """Pullout client"""
    if debug:
        enable_debug()
    
    db = SQLiteDb(overwrite_db=reset)
    if init:
        db.create_user(init)
        exit(0)
    
    if sync:
        user = db.get_user()
        if not user:
            if init:
                db.create_user(init)
                exit(0)
            else:
                print("No user found. Use pullout --init 'server_url.com' to create a new user.")
                exit(1)
        try:
            conn = DavConnection(user['server_url'], user['username'], user['password'], db)
        except Exception as e:
            print("Failed to connect to CardDav server: {}".format(e))
            exit(1)
        conn.sync_with_db()

    elif del_addressbook:
        db.delete_addressbook(del_addressbook)

    elif print_all:
        vcards = db.get_all_vcards()
        printer.print_vcards(vcards)
    
    elif print_vcards:
        vcards = db.get_addressbook_vcards(addressbook)
        printer.print_vcards(vcards)

    elif print_addressbooks:
        printer.print_addressbooks(db)

    elif remove:
        db.delete_vcard(remove)

    elif add_interactively:
        vcard_obj = printer.read_data_interactively()
        db.add_vcard(vcard_obj, addressbook)

    # Modify vcard
    elif modify_id:
        vcard_dict = db.get_vcard(modify_id)
        modified_vcard_dict = printer.modify_vcard_interactive(vcard_dict)
        if modified_vcard_dict:
            db.modify_vcard(modify_id, modified_vcard_dict)
        else:
            print("Nothing was changed")
    
    elif create_addr:
        db.create_addressbook(create_addr)

    elif addressbook and not name and not tel and not email and not org:
        db.change_addressbook(addressbook)

    elif images:
        print("Processing images...")

        from .image_processing import send_images
        from .vobj import vCardObject
        import time

        start = time.time()
        results = send_images(images)
        end = time.time()

        for result in results:
            if not result or result == {}:
                print("No entities found")
                continue
            elif 'FN' not in result and 'ORG' not in result:
                print("No name found, instead found:\n {}".format(result))
                continue
            if DEBUG:
                print(f"\nProcessing took {end - start} seconds\n")
            vcard_result = vCardObject(vcard_dict=result)
            printer.print_vcard(vcard_result.get_vcard_dict())
            print()
            db.add_vcard(vcard_result, addressbook)

    # Query database. If no option provided, output all vcards
    else:
        search_options = {'FN': name, 'TEL': tel, 'EMAIL': email, 'ORG': org}
        queries = db.query(search_options, addressbook)
        # Print to stdout or generate PDF
        if not export:
            printer.print_vcards(queries)
        else:
            from .pdf_gen import generate_pdf
            generate_pdf(queries, export)
        
