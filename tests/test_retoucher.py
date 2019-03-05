import os
import sys

import pytest
from PIL import Image
from PIL.ExifTags import TAGS

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import inscription.retoucher

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
        img = Image.open(chdir + '\\images\\IMG_0486.jpg')
        exif = inscription.retoucher.get_exif(img)

        expected = 'Canon EOS M6'
        expected2 = 'EF-M22mm f/2 STM'
        expected3 = 8
        expected4 = 800

        actual = exif['Model']
        actual2 = exif['LensModel']
        actual3 = exif['FNumber'][0] / exif['FNumber'][1]
        actual4 = exif['ISOSpeedRatings']
        
        assert actual == expected
        assert actual2 == expected2
        assert actual3 == expected3
        assert actual4 == expected4
