import unittest
import pandas as pd
import shutil
from datetime import datetime
from metadata_tools import MetadataTools
class TestMetadataTools(unittest.TestCase):

    def setUp(self):
        self.path = "tests/test_images/test_image.jpg"
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
        exif_dict = {"XMP:CreatorCity": 'San Francisco', 'IPTC:CopyrightNotice': 'CaliforniaAcademy',
                     'XMP:CreateDate': f'{datetime_test}'}
        self.md.write_exif_tags(exif_dict=exif_dict)
        exif_return = self.md.read_exif_tags()

        self.assertEqual("San Francisco", exif_return['XMP:CreatorCity'])
        self.assertEqual('CaliforniaAcademy', exif_return['IPTC:CopyrightNotice'])
        self.assertEqual(str(f'{datetime_test}'), str(exif_return['XMP:CreateDate']))

    def test_invalid_exif_tags(self):
        exif_dict = {'EXIF:TEST1': 'Samsung', 'IPTC:CopyrightNotice': 'CaliforniaAcademy', 'EXIF:ApertureValid': '1.5'}
        with self.assertRaises(ValueError) as context:
            self.md.write_exif_tags(exif_dict=exif_dict)

        self.assertEqual(str(context.exception),
                         "Invalid keys in exif_dict, check exif "
                         "constants:{'EXIF:TEST1': False, 'IPTC:CopyrightNotice': True, 'EXIF:ApertureValid': False}")

    def tearDown(self):
        del self.md
        shutil.copyfile("tests/test_images/image_backup.jpg", "tests/test_images/test_image.jpg")


