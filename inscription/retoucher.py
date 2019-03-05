from PIL import Image
from PIL.ExifTags import TAGS

def calc_height(pic_width, pic_height, width):
    return round(width / pic_width * pic_height,3)

def get_exif(img):
    exif = img._getexif()

    exif_table = {}

    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    return exif_table

