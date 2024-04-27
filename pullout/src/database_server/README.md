## Description
Database server is where CardDav server runs and PostgreSQL which stores this data.

## Development
### Postgresql setup
TODO. You can also use ansible script to set that up. And add the below setup to that VM.

### PHP setup [Linux]
Install php dependencies
```bash
sudo apt install php php-pgsql
```

Copy paste to terminal to install composer in current directory
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'e21205b207c3ff031906575712edab6f13eb0b361f2085f1f1237b7126d785e826a450292b6cfd1d64d92e6563bbde02') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

Move to /usr/local/bin to make it globally available command:
```bash
sudo mv composer.phar /usr/local/bin/composer
```

Uncomment php extensions: `iconv` `pdo_pgsql` `pgsql`
```bash
sudo nano /etc/php/php.ini
```
E.g: `;extension: iconv` to `extension: iconv`

Install sabredav dependencies
```bash
composer install
```

Run server locally with:
```bash
composer local
```

### Composer install on Windows
Look over [install guide](https://getcomposer.org/download/)


## Testing out
### Automatic:
```bash
composer tests
```

### Manual
You can download a carddav client and add this server. [List of clients](https://sabre.io/dav/clients/)

For now it has been tested to be working with "Evolution" CardDav client

##### CURL commands for testing on terminal

If you do not have `xmllint`, you can remove the pipe, it is only for easier reading of the output

Get principal href
```bash
curl -u all:all -X PROPFIND \
-H "Content-Type: application/xml" \
-H "Depth: 0" \
-d '<?xml version="1.0"?>
    <d:propfind xmlns:d="DAV:">
      <d:prop>
        <d:current-user-principal />
      </d:prop>
    </d:propfind>' \
--digest \
http://localhost:8080 | xmllint --format -
```
Get addressbook href
```bash
curl -u all:all -X PROPFIND \
-H "Content-Type: application/xml" \
-H "Depth: 0" \
-d '<?xml version="1.0"?>
    <d:propfind xmlns:d="DAV:" xmlns:card="urn:ietf:params:xml:ns:carddav">
      <d:prop>
        <card:addressbook-home-set />
      </d:prop>
    </d:propfind>' \
--digest \
http://localhost:8080/principals/all/ | xmllint --format -
```

List all the addressbooks for the user
```bash
curl -u all:all -X PROPFIND \
-H "Content-Type: application/xml" \
-H "Depth: 1" \
-d '<?xml version="1.0"?>
    <d:propfind xmlns:d="DAV:" xmlns:cs="http://calendarserver.org/ns/">
      <d:prop>
        <d:resourcetype />
        <d:displayname />
        <cs:getctag />
      </d:prop>
    </d:propfind>' \
--digest \
http://localhost:8080/addressbooks/all/ | xmllint --format -
```

Find sync token
```bash
curl -u all:all -X PROPFIND \
-H "Content-Type: application/xml" \
-H "Depth: 0" \
-d '<d:propfind xmlns:d="DAV:" xmlns:cs="http://calendarserver.org/ns/">
      <d:prop>
        <d:displayname />
        <cs:getctag />
        <d:sync-token />
      </d:prop>
    </d:propfind>' \
--digest \
http://localhost:8080/addressbooks/all/myAddressBook | xmllint --format -
```

Receive changes since last sync
```bash
curl -u all:all -X REPORT \
-H "Content-Type: application/xml" \
-d '<d:sync-collection xmlns:d="DAV:">
      <d:sync-token>http://sabredav.org/ns/sync/3</d:sync-token>
      <d:sync-level>1</d:sync-level>
      <d:prop>
        <d:getetag/>
      </d:prop>
    </d:sync-collection>' \
--digest \
http://localhost:8080/addressbooks/all/myAddressBook | xmllint --format -
```



Downloading objects
```bash
curl -u all:all -X PROPFIND \
-H "Content-Type: text/xml" \
-H "Depth: 1" \
-d '<propfind xmlns="DAV:">
      <prop>
        <getetag xmlns="DAV:" />
        <address-data xmlns="urn:ietf:params:xml:ns:carddav" />
      </prop>
    </propfind>' \
--digest \
http://localhost:8080/addressbooks/all/myAddressBook/ | xmllint --format -
```

Get one vcard data
```bash
curl -u all:all \
-X GET \
-H "Accept: text/vcard" \
--digest \
http://localhost:8080/addressbooks/all/myAddressBook/example_contact.vcf
```

To create new addressbook
```bash
curl -X MKCOL -H "Content-Type: application/xml" \
  -d '<?xml version="1.0" encoding="utf-8" ?>
      <D:mkcol xmlns:D="DAV:" xmlns:card="urn:ietf:params:xml:ns:carddav">
        <D:set>
          <D:prop>
            <D:resourcetype>
                <D:collection/>
                <card:addressbook/>
            </D:resourcetype>
            <D:displayname>NewAddressBook</D:displayname>
          </D:prop>
        </D:set>
      </D:mkcol>' \
  http://localhost:8080/addressbooks/users/NewAddressBook
```

Delete addressbook
```bash
curl -X DELETE \
  http://localhost:8080/addressbooks/users/NewAddressBook
```

Put a new vcard
```bash
curl -u all:all -X PUT -H "Content-Type: text/vcard" \
--data 'BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:123456789
EMAIL:john.doe@example.com
END:VCARD' \
--digest \
http://localhost:8080/addressbooks/all/myAddressBook/example_contact.vcf
```

Delete vcard
```bash
curl -X DELETE \
  http://localhost:8080/addressbooks/users/NewAddressBook/example_contact.vcf
```

Create new user, it also creates a new adressbooks folder:
http://localhost:8080/addressbooks/new_user
```bash
curl -X MKCOL -H "Content-Type: application/xml" \
  -d '<?xml version="1.0" encoding="utf-8" ?>
      <D:mkcol xmlns:D="DAV:">
        <D:set>
          <D:prop>
            <D:resourcetype>
                <D:principal/>
            </D:resourcetype>
            <D:displayname>new_user</D:displayname>
          </D:prop>
        </D:set>
      </D:mkcol>' \
  http://localhost:8080/principals/new_user
```

Don't know how to delete user ;)


