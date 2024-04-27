from typing import List, Dict
from .backend import SQLiteDb
from .vobj import vCardObject

key_map = { 'VCARD_ID': 'id', \
            'ADDRESSBOOK_NAME': 'addressbook name', \
            'FN': 'Name', \
            'TEL':'Telephone',\
            'EMAIL': 'Email',\
            'ORG': 'Organization', \
            'TITLE': 'Title', \
            'URL': 'Website',\
            'ADR': 'Address'
          }

def print_vcards(vcards: List[Dict]) -> None:
    """Print formatted vcards to stdout."""
    if not vcards:
        print("No contacts found")
        return
    # Sort by addressbook name
    vcards.sort(key=lambda x: x['ADDRESSBOOK_NAME'])

    index = 0
    length = len(vcards)
    while index < length:
        addressbook_name = vcards[index]['ADDRESSBOOK_NAME']
        print("[{}]".format(addressbook_name))

        while index < length and vcards[index]['ADDRESSBOOK_NAME'] == addressbook_name:
            vcards[index].pop('ADDRESSBOOK_NAME')
            print_vcard(vcards[index])
            index += 1

def print_vcard(vcard: dict) -> None:
    """Print formatted vcard to stdout"""
    print()
    if vcard is None or not vcard.items():
        print("Nothing was found")
    for key, value in vcard.items():
        if key in key_map and value != None and value != "":
            print("{}: {}".format(key_map[key], value))

def read_data_interactively() -> vCardObject:
    """Add vcard interactively"""
    print("You can leave fields empty except name")
    read_vcard = {}
    read_vcard['FN'] = input("Name: ")
    if read_vcard['FN'] == '':
        print("Name cannot be empty")
        exit(0)
    read_vcard['TEL'] = input("Telephone: ")
    read_vcard['EMAIL'] = input("Email: ")
    read_vcard['ORG'] = input("Organization: ")
    read_vcard['TITLE'] = input("Title: ")
    read_vcard['URL'] = input("URL: ")
    read_vcard['STREET'] = input("Street: ")
    read_vcard['CITY'] = input("City: ")
    read_vcard['COUNTRY'] = input("Country: ")
    read_vcard['POSTCODE'] = input("Postcode: ")
    vcard = vCardObject(vcard_dict=read_vcard)
    return vcard

def print_addressbooks(db: SQLiteDb) -> None:
    """Print all addressbooks"""
    addressbooks = db.get_addressbooks()
    active_addressbook_name = db.get_active_addressbook()[1]
    for addressbook in addressbooks:
        addr_name = addressbook['addressbook_name']
        ctag = addressbook['ctag']
        count = db.get_addressbook_vcards(addr_name).__len__()
        if addr_name == active_addressbook_name:
            print("{}: {} contacts (active), ctag={}".format(addr_name, count, ctag))
        else:
            print("{}: {} contacts, ctag={}".format(addr_name, count, ctag))

def modify_vcard_interactive(vcard_dict: dict) -> dict:
    """Modify vcard interactively"""
    if vcard_dict is None:
        print("Nothing was found")
        return
    has_changed = False
    for key, value in vcard_dict.items():
        if key == 'VCARD_ID':
            continue
        new_value = input("{} ({}): ".format(key_map[key], value))
        if new_value != '':
            print("Changed {} from {} to {}".format(key_map[key], value, new_value))    
            vcard_dict[key] = new_value
            has_changed = True
    
    if has_changed:
        # Remove vcard_id because we will be deleting old one and inputting new one
        vcard_dict.pop('VCARD_ID')
        # Make sure vcard_dict values are empty strings if they are None
        for key, value in vcard_dict.items():
            if value is None:
                vcard_dict[key] = ''
        return vcard_dict
    else:
        return None