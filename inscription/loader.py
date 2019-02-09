import os
import glob
from pathlib import Path

from inscription.settings import Settings

class Loader(object):

    def md_list(self, path):
        path = Path(path)
        md_list = path.glob('*.md')
        md_list = [os.path.basename(x) for x in md_list]
        return md_list

    def template_list(self, path):
        path = Path(path)
        template_list = path.glob('*_template.html')
        template_list = [os.path.basename(x) for x in template_list]
        return template_list

    def md_sorted_list(self, path, count):
        md_list = glob.glob(path + '/*.md')
        md_sorted_list = sorted(md_list,key=os.path.getatime)
        return md_sorted_list[0:count]