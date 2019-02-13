import os
import glob
from pathlib import Path

from inscription.settings import Settings

class Loader(object):

    def md_list(self, path, count):
        path = Path(path)
        md_list = path.glob('*_*_*.md')
        md_list = [os.path.basename(x) for x in md_list]
        md_list = sorted(md_list, reverse=True)

        if count == -1:
            return md_list
        else :
            return md_list[0:count]

    def template_list(self, path):
        path = Path(path)
        template_list = path.glob('*_template.html')
        template_list = [os.path.basename(x) for x in template_list]
        return template_list

    def entries_directory_list(self):
        return 0