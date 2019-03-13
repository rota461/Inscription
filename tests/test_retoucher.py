import os
import sys

import pytest
from PIL import Image
from PIL.ExifTags import TAGS

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import inscription.retoucher
import inscription.settings

class TestRetoucher(object):

    def test_calc_height(self):
        expected = 735
        expected2 = 408.333

        actual = inscription.retoucher.calc_height(2000, 3000, 490)
        actual2 = inscription.retoucher.calc_height(3000, 2500, 490)

        assert actual == expected
        assert actual2 == expected2

    def test_get_exif(self):
        chdir = os.path.abspath(os.path.dirname(__file__))
        img = Image.open(chdir + '/images/IMG_0486.JPG'.replace('/',os.path.sep))
        exif = inscription.retoucher.get_exif(img)

        expected = 'Canon EOS M6'
        expected2 = 'EF-M22mm f/2 STM'
        expected3 = 8
        expected4 = 800

        actual = exif['Model']
        actual2 = exif['LensModel']
        actual3 = exif['FNumber'][0] / exif['FNumber'][1]
        actual4 = exif['ISOSpeedRatings']
        
        img.close()

        assert actual == expected
        assert actual2 == expected2
        assert actual3 == expected3
        assert actual4 == expected4

    def test_generate_image_data(self):
        settings = inscription.settings.Settings()
        chdir = os.path.dirname(os.path.abspath(__file__))
        settings.read_config(chdir)
        retoucher = inscription.retoucher.Retoucher(settings)

        img_data = retoucher.generate_image_data('IMG_0486')

        expected_name = 'IMG_0486'
        expected_description = 'mediatheque'
        expected_width = 490
        expected_height = 326.83
        expected_model = 'Canon EOS M6'
        expected_lens_model = 'EF-M22mm f/2 STM'
        expected_f = 8
        expected_iso = 800

        actual_name = img_data.img_name
        actual_description = img_data.description
        actual_width = img_data.width
        actual_height = img_data.height
        actual_model = img_data.model
        actual_lens_model = img_data.lens_model
        actual_f = img_data.f
        actual_iso = img_data.iso

        assert actual_name == expected_name
        assert actual_description == expected_description
        assert actual_width == expected_width
        assert actual_height == expected_height
        assert actual_model == expected_model
        assert actual_lens_model == expected_lens_model
        assert actual_f == expected_f
        assert actual_iso == expected_iso

    def test_set_image_height(self):
        
        class IMG(object):
            def __init__(self, height):
                self.height = height

        img_list = [IMG(100), IMG(200), IMG(300), IMG(400), IMG(500), IMG(600)]

        inscription.retoucher.set_image_height(img_list)

        expected = 0
        expected2 = 0
        expected3 = 120
        expected4 = 220
        expected5 = 440
        expected6 = 640

        actual = img_list[0].height
        actual2 = img_list[1].height
        actual3 = img_list[2].height
        actual4 = img_list[3].height
        actual5 = img_list[4].height
        actual6 = img_list[5].height

        assert actual == expected
        assert actual2 == expected2
        assert actual3 == expected3
        assert actual4 == expected4
        assert actual5 == expected5
        assert actual6 == expected6