from unittest import TestCase
from pullout.backend import SQLiteDb
from pullout.vobj import vCardObject

class TestBackend(TestCase):
    def test_addressbooks(self):
        db = SQLiteDb(db_path="tests/assets/db/addressbooks.db", overwrite_db=True, should_log=False)
        # Should create default addressbook
        addressbook_names = db.get_addressbooks()
        self.assertIn('default', addressbook_names[0]['addressbook_name'])
        # Create a couple more addressbooks
        db.create_addressbook('g1')
        db.create_addressbook('g2')
        # Deleted addressbook should not be able to access
        db.delete_addressbook('g1')
        try:
            db.change_addressbook('g1')
            self.fail("Should have failed")
        except Exception as e:
            pass
        # Changed addressbook should change who is in use
        db.change_addressbook('g2')
        in_use = db.get_active_addressbook()
        self.assertEqual(in_use, 'g2')
        # Deleting addressbook should fail because it is in use
        try:
            db.delete_addressbook('g2')
            self.fail("Should have failed")
        except Exception as e:
            pass
        # Creating addressbook with no name should fail
        try:
            db.create_addressbook()
            self.fail("Should have failed")
        except Exception as e:
            pass
    
    def test_vcards(self):
        db = SQLiteDb("tests/assets/db/vcards.db", overwrite_db=True, should_log=False)
        # Get vcard data from assets/vcards/*.vcf
        vcard_data = [None] * 5
        for i in range(0, 5):
            with open("tests/assets/vcards/ex{}.vcf".format(i+1), 'r') as f:
                file_data = f.read()
            vcard_data[i] = vCardObject(file_data).get_vcard_dict()

        # Add vcard data to db
        db.add_vcard(vcard_data[0])
        vcards = db.get_addressbook_vcards()
        # Check the first vcard if it has the name "John Doe"
        self.assertIn('John Doe', vcards[0]['fn'])
        db.delete_vcard(vcards[0]['id'])
        vcards = db.get_addressbook_vcards()
        self.assertEqual(vcards, [])
        # Add all vcards
        for i in range(0, 5):
            db.add_vcard(vcard_data[i])
        vcards = db.get_addressbook_vcards()
        # Check if all vcards were added
        self.assertEqual(len(vcards), 5)
        # Delete third vcard
        db.delete_vcard(vcards[2]['id'])
        