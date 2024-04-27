import unittest

from .utils import check_valid_list

class TestPhoneRegex(unittest.TestCase):
    def test_number_formats(self):
        all_phones = [
            "+37069918736",
            "+370 6 99 18736"
        ]
        # found = regex.list_phones(" ".join(all_phones))
        # check_list(self, found, all_phones)
