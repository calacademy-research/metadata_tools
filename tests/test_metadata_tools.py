import unittest
import pandas as pd
import shutil
from metadata_tools import MetadataTools
from EXIF_constants import EXIFConstants
import xml.etree.ElementTree as ET
import subprocess

class TestMetadataTools(unittest.TestCase):

    @classmethod
    def get_exif_tags(self):
        """Helper method to extract complete list of exif terms compatible with exiftool"""
        result = subprocess.run(['exiftool', '-listx', '-f'], capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(f"Error running exiftool: {result.stderr}")

        xml_output = result.stdout

        #XML output --> string
        root = ET.fromstring(xml_output)

        tags = set()
        for table in root.findall('table'):
            for tag in table.findall('tag'):
                tag_name = tag.get('name')
                tags.add(tag_name)

            # Check for IFD0 group
            if table.get('name') == 'IFD0':
                for tag in table.findall('tag'):
                    tag_name = f"IFD0:{tag.get('name')}"
                    tags.add(tag_name)

        return tags


    def setUp(self):
        self.path = "tests/test_images/test_image.jpg"
        self.md = MetadataTools(path=self.path)
        self.valid_exif_tags = self.get_exif_tags()
        shutil.copyfile("tests/test_images/test_image.jpg", "tests/test_images/image_backup.jpg")


    def test_read_exif_tags(self):
        """tests exif read function"""
        exif_dict = self.md.read_exif_tags()
        self.assertFalse(pd.isna(exif_dict))
        self.assertNotEqual(exif_dict, {})
        self.assertEqual(exif_dict['EXIF:LensMake'], 'Apple')

    def test_write_exif_tags(self):
        """tests exif attach function"""
        exif_dict = {'EXIF:LensMake': 'Samsung', 'IPTC:City': 'San Boston', 'EXIF:ApertureValue': '1.5'}
        self.md.write_exif_tags(exif_dict=exif_dict)
        exif_return = self.md.read_exif_tags()
        self.assertEqual("Samsung", exif_return['EXIF:LensMake'])
        self.assertEqual('San Boston', exif_return['IPTC:City'])
        self.assertEqual('1.5', exif_return['EXIF:ApertureValue'])

    def test_accepted_exif_tags(self):
        """test whether the list of EXIFConstants are accepted tags in exiftools"""
        exif_constants = {attr: value for attr, value in EXIFConstants.__dict__.items() if
                          not callable(value) and not attr.startswith("__")}

        for tag_name, tag_value in exif_constants.items():
            if tag_value.startswith("EXIF:"):
                parts = tag_value.split(':')
                actual_tag = parts[-1]  # Get the last part of the split
                if actual_tag.startswith("IFDO:"):  # Check if IFD0 is present
                    actual_tag = actual_tag[5:]
                self.assertIn(actual_tag, self.valid_exif_tags,
                              f"EXIF tag {tag_value} ({tag_name}) is not a valid EXIF tag")

    def tearDown(self):
        del self.md
        shutil.copyfile("tests/test_images/image_backup.jpg", "tests/test_images/test_image.jpg")


