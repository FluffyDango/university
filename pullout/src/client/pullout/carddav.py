import requests
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree as ET
from xml.dom.minidom import parseString
from .backend import SQLiteDb
from .vobj import vCardObject
from typing import List, Dict

class DavConnection():
    def __init__(self, server_url: str, username: str, password: str, db: SQLiteDb) -> None:
        if server_url[0:4] != 'http':
            server_url = 'http://' + server_url
        self.base_url = server_url
        self.db = db
        self.session = requests.Session()
        self.session.auth = HTTPDigestAuth(username, password)
        self.prin_href = self._discover_principal_href()
        self.addr_href = self._discover_addressbook_href()
        self.addressbooks = self._discover_addressbooks()
        # print(self.addressbooks)

    def __del__(self):
        self.session.close()

    def _discover_principal_href(self) -> str:
        """Discover principal URL"""
        headers = {
            'Content-Type': 'application/xml',
            'Depth': '0',
        }
        xml_payload = '''
            <d:propfind xmlns:d="DAV:">
              <d:prop>
                <d:current-user-principal />
              </d:prop>
            </d:propfind>
        '''

        r = self.session.request('PROPFIND', self.base_url, headers=headers, data=xml_payload)

        if r.status_code != 207:
            raise Exception("Failed to discover principal URL")
            
        xml_response = ET.fromstring(r.text)
        principal_element = xml_response.find(".//{DAV:}current-user-principal/{DAV:}href")

        if principal_element is None:
            raise Exception("Principal URL not found in the response")
        
        return principal_element.text
    
    def _discover_addressbook_href(self) -> str:
        """Discover addressbook URL"""
        headers = {
            'Content-Type': 'application/xml',
            'Depth': '0',
        }
        xml_payload = '''
            <d:propfind xmlns:d="DAV:" xmlns:card="urn:ietf:params:xml:ns:carddav">
                <d:prop>
                    <card:addressbook-home-set />
                </d:prop>
            </d:propfind>
        '''

        r = self.session.request('PROPFIND', self.base_url+self.prin_href, headers=headers, data=xml_payload)

        if r.status_code != 207:
            raise Exception("Failed to discover addressbook URL")
            
        xml_response = ET.fromstring(r.text)
        propstat_element = xml_response.find(".//{DAV:}propstat")
        
        if propstat_element is None:
            raise Exception("propstat element not found in the response")

        addressbook_element = propstat_element.find(".//{urn:ietf:params:xml:ns:carddav}addressbook-home-set/{DAV:}href")

        if addressbook_element is None:
            raise Exception("Addressbook URL not found in the response")
        
        return addressbook_element.text

    def _discover_addressbooks(self) -> List[Dict]:
        """Get addressbooks"""
        headers = {
            'Content-Type': 'application/xml',
            'Depth': '1',
        }
        xml_payload = '''
           <d:propfind xmlns:d="DAV:" xmlns:cs="http://calendarserver.org/ns/">
                <d:prop>
                    <d:resourcetype />
                    <d:displayname />
                    <cs:getctag />
                </d:prop>
            </d:propfind>
        '''

        r = self.session.request('PROPFIND', self.base_url+self.addr_href, headers=headers, data=xml_payload)

        if r.status_code != 207:
            raise Exception("Failed to get addressbooks, " + str(r.status_code) + " " + r.text)

        xml_response = ET.fromstring(r.text)
        response_elements = xml_response.findall(".//{DAV:}response")

        if response_elements is None:
            raise Exception("Response elements not found in the response")

        addressbooks = []
        
        for response_element in response_elements:
            href_element = response_element.find(".//{DAV:}href")
            resourcetype_element = response_element.find(".//{DAV:}resourcetype")

            if href_element is not None and resourcetype_element is not None:
                if resourcetype_element.find(".//{urn:ietf:params:xml:ns:carddav}addressbook") is not None:
                    addressbook_info = {
                        'href': href_element.text,
                        'displayname': response_element.find(".//{DAV:}displayname").text,
                        'getctag': response_element.find(".//{http://calendarserver.org/ns/}getctag").text,
                    }
                    addressbooks.append(addressbook_info)

        return addressbooks
    
    def download_data(self) -> dict:
        """Download vcards"""
        vcards_info = {}
        for addressbook in self.addressbooks:
            vcards_addr = self.download_vcards_from_addressbook(addressbook)
            vcards_info[addressbook['displayname']] = vcards_addr
        return vcards_info
    
    def download_vcards_from_addressbook(self, addressbook: dict) -> List[Dict]:
        """Download vcards"""
        headers = {
            'Content-Type': 'application/xml',
            'Depth': '1',
        }
        xml_payload = '''
           <propfind xmlns="DAV:">
                <prop>
                    <getetag xmlns="DAV:" />
                    <address-data xmlns="urn:ietf:params:xml:ns:carddav" />
                </prop>
            </propfind>
        '''

        r = self.session.request('PROPFIND', self.base_url+addressbook['href'], headers=headers, data=xml_payload)

        if r.status_code != 207:
            raise Exception("Failed to get vcards")
        
        # print(parseString(r.text).toprettyxml())
        xml_response = ET.fromstring(r.text)
        response_elements = xml_response.findall(".//{DAV:}response")

        if response_elements is None:
            raise Exception("Response elements not found in the response")

        vcards_info = []
        
        for response_element in response_elements:
            href_element = response_element.find(".//{DAV:}href")
            etag_element = response_element.find(".//{DAV:}getetag")
            card_data_element = response_element.find(".//{urn:ietf:params:xml:ns:carddav}address-data")

            # If href is the same as addressbook href, skip it
            if href_element.text == addressbook['href']:
                continue

            # If elements are not none, add them to vcards
            if href_element is not None and etag_element is not None and card_data_element is not None:
                vcard_info = {
                    'href': href_element.text,
                    'etag': etag_element.text,
                    'card_data': card_data_element.text,
                }
                vcards_info.append(vcard_info)

        return vcards_info
    
    def upload_vcard(self, vcard: vCardObject, addressbook: str) -> None:
        """Upload vcard to addressbook"""
        headers = {
            'Content-Type': 'text/vcard',
            'If-None-Match': '*',
        }
        data = vcard.get_vcard_string()
        r = self.session.request('PUT', self.base_url+self.addr_href+addressbook+'/'+str(hash(vcard))+'.vtf',
                                 headers=headers, data=data)
        if r.status_code != 201:
            raise Exception("Failed to upload vcard")

    def get_newest_addressbook_changes(self, addressbook_name: str, ctag: int) -> None:
        """Update addressbook ctag and check what vcards need to be updated"""
        self.db.update_addressbook_ctag(addressbook_name, ctag)
        headers = {
            'Content-Type': 'application/xml',
            'Depth': '1',
        }
        xml_payload = '''
            <propfind xmlns="DAV:">
                <prop>
                    <getetag xmlns="DAV:" />
                </prop>
            </propfind>
        '''
        href = self.addr_href+addressbook_name+'/'
        r = self.session.request('PROPFIND', url=self.base_url+href, headers=headers, data=xml_payload)

        if r.status_code != 207:
            raise Exception("Failed to update addressbook")
        print(parseString(r.text).toprettyxml())

        xml_response = ET.fromstring(r.text)
        response_elements = xml_response.findall(".//{DAV:}response")

        if response_elements is None:
            raise Exception("Response elements not found in the response")

        local_vcards = self.db.get_addressbook_vcards(addressbook_name)
        local_href_list = [vcard['href'] for vcard in local_vcards]
        local_etag_list = [vcard['etag'] for vcard in local_vcards]
        server_href_list = []
        server_etag_list = []
        
        for response_element in response_elements:
            href_element = response_element.find(".//{DAV:}href")
            etag_element = response_element.find(".//{DAV:}getetag")

            # If href is the same as addressbook href, skip it
            if href_element.text == href:
                continue

            # If elements are not none, add them to vcards
            if href_element is not None and etag_element:
                server_href_list.append(href_element.text)
                server_etag_list.append(etag_element.text)

        for href, etag in zip(local_href_list, local_etag_list):
            if href not in server_href_list:
                self.db.delete_vcard_by_href(href)
            elif etag != server_etag_list[server_href_list.index(href)]:
                self.db.delete_vcard_by_href(href)

    def update_vcard(self, vcard: vCardObject, addressbook: str) -> None:
        """Update vcard"""
        pass

    def put_local_vcards_to_server(self, addressbook_name: str) -> None:
        """Put local vcards to server"""
        local_vcards = self.db.get_addressbook_vcards(addressbook_name)
        local_href_list = [vcard['href'] for vcard in local_vcards]
        local_etag_list = [vcard['etag'] for vcard in local_vcards]
        headers = {
            'Content-Type': 'text/vcard',
            'If-None-Match': '*',
        }
        for href, etag in zip(local_href_list, local_etag_list):
            if href not in self.addressbooks:
                self.db.delete_vcard_by_href(href)
            elif etag != self.addressbooks[self.addressbooks.index(href)]:
                self.db.delete_vcard_by_href(href)

    def sync_with_db(self) -> None:
        """
        Sync with database.
        Get all server ctags and check with local database ctags
        If ctags are the same, skip
        If ctags are different, download vcard and update database
        If local database does not have addressbook, create it and populate it with vcards
        """

        local_addressbooks = self.db.get_addressbooks()

        for addressbook in self.addressbooks:
            found = False
            for local_addressbook in local_addressbooks:
                if addressbook['displayname'] == local_addressbook['addressbook_name']:
                    found = True
                    if addressbook['getctag'] != local_addressbook['ctag']:
                        self.get_newest_addressbook_changes(addressbook['displayname'], addressbook['getctag'])
                        break
                    self.put_local_vcards_to_server(addressbook['displayname'])
            if not found:
                self.db.create_addressbook(addressbook['displayname'], addressbook['getctag'])
                vcards = self.download_vcards_from_addressbook(addressbook)
                for vcard in vcards:
                    self.db.add_vcard(vCardObject(vcard['card_data']), addressbook['displayname'])