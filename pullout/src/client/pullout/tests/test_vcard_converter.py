import unittest
from pullout.vobj import vCardObject

class TestVcardConverter(unittest.TestCase):
    def test_vcard_regular(self):
        vc = vCardObject()
        vc.append_fn("Renaldas Narbutas")
        vc.append_email("renaldas.narbutas@mif.stud.vu.lt")
        vc.append_org("Vilniaus Universitetas")
        vc.append_title("Studentas")
        vc.append_address("Didlaukio g. 59", "Vilnius", "Lithuania")
        vcString = vc.get_vcard()
        vcString = vcString.strip()
        valid_vcard = '\
BEGIN:VCARD\r\nVERSION:3.0\r\n\
ADR:;;Didlaukio g. 59;Vilnius;;;Lithuania\r\n\
EMAIL:renaldas.narbutas@mif.stud.vu.lt\r\n\
FN:Renaldas Narbutas\r\n\
N:Narbutas;Renaldas;;;\r\n\
ORG:Vilniaus Universitetas\r\n\
TITLE:Studentas\r\n\
END:VCARD'
        self.assertEqual(vcString, valid_vcard)

    def test_vcard_address(self):
        vc = vCardObject()
        try:
            vc.append_address(COUNTRY="Vilnius")
            self.fail("append_address Should have thrown an exception because it needs to have street")
        except:
            pass
    
    def test_vcard_basic(self):
        vc = vCardObject()
        vc.append_fn("Saulius Andrius Katkus")
        vcString = vc.get_vcard()
        
        valid_vcard = '\
BEGIN:VCARD\r\nVERSION:3.0\r\n\
FN:Saulius Andrius Katkus\r\n\
N:Katkus;Saulius;Andrius;;\r\n\
END:VCARD\r\n'
        self.assertEqual(vcString, valid_vcard)
        