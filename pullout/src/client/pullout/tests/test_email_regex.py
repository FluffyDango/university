import unittest
from .utils import check_valid_list
from .utils import check_invalid_list

class TestEmailRegex(unittest.TestCase):
    def test_email(self):
        # Taken from Wikipedia and
        # https://codefool.tumblr.com/post/15288874550/list-of-valid-and-invalid-email-addresses
        valid_emails = [
            "renaldas.narbutas@mif.stud.vu.lt",
            "robot123@gmail.com",
            "info@nowork.lt",
            "jdsk@bob.com.lol",
            "popop@coco.com",
            "email@example.com",
            "firstname.lastname@example.com",
            "email@subdomain.example.com",
            "firstname+lastname@example.com",
            "email@123.123.123.123",
            "email@[123.123.123.123]",
            "email@example.com",
            "1234567890@example.com",
            "email@example-one.com",
            "_______@example.com",
            "email@example.name",
            "email@example.museum",
            "email@example.co.jp",
            "firstname-lastname@example.com",
            "simple@example.com",
            "very.common@example.com",
        ]
        invalid_emails = [
            "@gmail.com",
            "email@",
            "email@.com",
            "email@examplecom",
            "email@example.co jp",
            "email@example.m useum",
            "email@example .com",
            "@example.com",
        ]
        # found = list_emails(" ".join(valid_emails))
        # check_valid_list(self, found, valid_emails)
        # found = list_emails(" ".join(invalid_emails))
        # check_invalid_list(self, found, invalid_emails)