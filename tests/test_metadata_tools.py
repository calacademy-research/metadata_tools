import unittest
import pandas as pd
import shutil
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
        self.assertEqual(exif_dict[272], 'iPhone XR')

    def test_write_exif_tags(self):
        pass

    def test_accepted_exif_tags(self):
        pass


    def tearDown(self):
        del self.md
        shutil.copyfile("tests/test_images/image_backup.jpg", "tests/test_images/test_image.jpg")


