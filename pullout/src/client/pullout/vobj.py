import vobject
import hashlib
from typing import List, Dict

class vCardObject:
    def __init__(self, vcard_str: str=None, vcard_dict: dict={}):
        if vcard_str is not None:
            self.vcard = vobject.readOne(vcard_str)

        elif vcard_dict is not None and vcard_dict != {}:
            self.vcard = vobject.vCard()

            # Handle address, name and telephone in a special manner
            addr = {}
            tel = []
            fn_added = False

            for key, value in vcard_dict.items():
                if value == None or value == "":
                    continue
                if key == 'STREET' or key == 'CITY' or key == 'COUNTRY' or key == 'POSTCODE':
                    addr[key] = value
                elif key == 'FN':
                    self.append_fn(value)
                    fn_added = True
                elif key == 'TEL':
                    tel.append(value)
                elif key == 'EMAIL':
                    self.append_email(value)
                elif key == 'TITLE':
                    self.append_title(value)
                elif key == 'ORG':
                    self.append_org(value)
                elif key == 'URL':
                    self.append_url(value)
                elif key == 'FAX':
                    pass
                elif key == 'REGION':
                    pass
                elif key == 'ADR':
                    pass
                else:
                    raise Exception("Unknown key: " + key)
            if addr != {}:
                self.append_address(**addr)
            if tel != []:
                self.append_tel(tel)
            if not fn_added and vcard_dict.get('ORG') is not None:
                self.append_fn(vcard_dict['ORG'])

        else:
            self.vcard = vobject.vCard()

    def __hash__(self) -> int:
        hashed = hashlib.md5(self.get_vcard_string().encode())
        result_int = int(hashed.hexdigest(), 16)
        return result_int

    def append_fn(self, name: str) -> None:
        # fn - formatted name string
        # example: fn="Renaldas Narbutas"
        self.vcard.add('fn')
        self.vcard.fn.value = name

    def append_tel(self, tel_list: list) -> None:
        for tel_number in tel_list:
            tel_instance = self.vcard.add('tel')
            tel_instance.value = tel_number


    def append_address(self, STREET: str="", CITY: str="", COUNTRY: str="", POSTCODE: str="") -> None:
        if STREET == "" and CITY == "" and COUNTRY == "" and POSTCODE == "":
            return
        self.vcard.add('adr')
        self.vcard.adr.value = vobject.vcard.Address(street=STREET, city=CITY, country=COUNTRY, code=POSTCODE)

    def append_email(self, email: str) -> None:
        self.vcard.add('email')
        self.vcard.email.value = email

    def append_title(self, job_title) -> None:
        self.vcard.add('title')
        self.vcard.title.value = job_title

    def append_org(self, organization: str) -> None:
        self.vcard.add('org')
        self.vcard.org.value = [ organization ]

    def append_url(self, url: str) -> None:
        self.vcard.add('url')
        self.vcard.url.value = url

    
    def get_vcard(self) -> str:
        return self.vcard.serialize()
    
    def get_vcard_string(self) -> str:
        return str(self.vcard.serialize())
    
    def get_vcard_dict(self) -> dict:
        lines = self.get_vcard().splitlines()
        vcard_dict = {}
        for line in lines:
            key, value = line.split(':', 1)
            if key == 'ADR':
                # Special case for address
                value = value.split(';')
                aggragated = ""
                if value[2] != "":
                    aggragated += value[2] + ", "
                if value[3] != "":
                    aggragated += value[3] + ", "
                if value[4] != "":
                    aggragated += value[4] + ", "
                if value[5] != "":
                    aggragated += value[5]
                vcard_dict['ADR'] = aggragated
            else:
                vcard_dict[key] = value
        return vcard_dict
    