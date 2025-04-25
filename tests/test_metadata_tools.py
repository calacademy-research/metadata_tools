import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
import shutil
from datetime import datetime
from cas_metadata_tools import MetadataTools
import platform



class TestMetadataTools(unittest.TestCase):

    def setUp(self):
        self.path = "tests/test_images/test_image.jpg"
        if platform.system() == "Darwin":
            encoding = "en_US.UTF-8"
        else:
            encoding = "C.UTF-8"

        self.md = MetadataTools(path=self.path)

        shutil.copyfile("tests/test_images/test_image.jpg", "tests/test_images/image_backup.jpg")


    def test_read_exif_tags(self):
        """tests exif read function"""
        exif_dict = self.md.read_exif_tags()
        self.assertFalse(pd.isna(exif_dict))
        self.assertNotEqual(exif_dict, {})
        self.assertEqual(exif_dict['EXIF:LensMake'], 'Apple')

    def test_write_exif_tags(self):
        """tests exif attach function"""
        datetime_test = datetime.now()
        datetime_test = datetime_test.strftime('%Y:%m:%d %H:%M:%S.%f')
        exif_dict = {"XMP:CreatorCity": 'San Francisco', 'IPTC:CopyrightNotice': '\u00A9 \u00B0 CaliforniaAcademy',
                     'XMP:CreateDate': f'{datetime_test}'}
        self.md.write_exif_tags(exif_dict=exif_dict)
        exif_return = self.md.read_exif_tags()

        self.assertEqual("San Francisco", exif_return['XMP:CreatorCity'])
        self.assertEqual('\u00A9 \u00B0 CaliforniaAcademy', exif_return['IPTC:CopyrightNotice'])
        self.assertEqual(str(f'{datetime_test}'), str(exif_return['XMP:CreateDate']))

    def test_invalid_exif_tags(self):
        exif_dict = {'EXIF:TEST1': 'Samsung', 'IPTC:CopyrightNotice': '\u00A9 \u00B0 CaliforniaAcademy', 'EXIF:ApertureValid': '1.5'}
        with self.assertRaises(ValueError) as context:
            self.md.write_exif_tags(exif_dict=exif_dict)

        self.assertEqual(str(context.exception),
                         "Invalid keys in exif_dict, check exif "
                         "constants:{'EXIF:TEST1': False, 'IPTC:CopyrightNotice': True, 'EXIF:ApertureValid': False}")

    def test_latin_1_encoding(self):
        self.md.path = os.path.join("tests", "test_images", "test_image_latin1.jpg")
        exif_dict = self.md.read_exif_tags()
        self.assertEqual(exif_dict['EXIF:Artist'], 'Johanna Loacker')
        # this is latin1 encoded
        self.assertEqual(exif_dict['EXIF:Copyright'], '© California Academy of Sciences licensed under CC BY-NC-SA')
    
    def test_other_encoding(self):
        self.md.path = os.path.join("tests", "test_images", "exif_gb2312.jpg")
        exif_dict = self.md.read_exif_tags()
        self.assertEqual(exif_dict['EXIF:UserComment'], '你好！')

    def tearDown(self):
        del self.md
        shutil.copyfile("tests/test_images/image_backup.jpg", "tests/test_images/test_image.jpg")


if __name__ == '__main__':
    unittest.main()
