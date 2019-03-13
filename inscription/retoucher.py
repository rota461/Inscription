import os

from PIL import Image
from PIL.ExifTags import TAGS

#from . import settings

class ImgData(object):
    def __init__(self, img_name, width, height, exif):
        self.img_name = img_name
        self.description = exif['ImageDescription']
        self.width = width
        self.height = height
        self.model = exif['Model']
        self.lens_model = exif['LensModel']
        self.f = exif['FNumber'][0] / exif['FNumber'][1]
        self.iso = exif['ISOSpeedRatings'] 

def calc_height(img_width, img_height, width):
    return round(width / img_width * img_height,3)

def get_exif(img):
    exif = img._getexif()

    exif_table = {}

    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    return exif_table

# set image height that will use in template.
def set_image_height(img_list):
    MARGIN = 20
    odd = 0
    even = 0
    for index, img in enumerate(img_list):
        tmp = img.height + MARGIN
        if(index % 2 == 1):
            img.height = odd
            odd += tmp
        else:
            img.height = even
            even += tmp

class Retoucher(object):
    def __init__(self, settings):
        self.settings = settings

    def generate_image_data(self, img_name):
        img = Image.open(self.settings.PATH['images'].replace('/', os.path.sep) + img_name+'.JPG')

        exif = get_exif(img)

        img_width = img.size[0]
        img_height = img.size[1]
        width = float(self.settings.IMG['width'])
        height = calc_height(img_width, img_height, width)

        img_data = ImgData(img_name, width, height, exif)
        img.close()

        return img_data
