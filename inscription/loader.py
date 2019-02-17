import os
import glob
from pathlib import Path

from inscription.settings import Settings

def md_list(path, count):
    path = Path(path)
    # entries or articles name must be yyyymmdd_serial_title.md.
    md_list = path.glob('*_*_*.md')
    md_list = [os.path.basename(x) for x in md_list]
    md_list = sorted(md_list, reverse=True)

    if count == -1:
        return md_list
    else :
        return md_list[0:count]

def template_list(path):
    path = Path(path)
    
    template_list = path.glob('*_template.html')
    template_list = [os.path.basename(x) for x in template_list]

    return template_list

def entries_dir_list(path):
    path = Path(path)
    tmp_list = path.glob('*')
    dir_list = []

    for x in tmp_list:
        if os.path.isdir(x):
            dir_list.append(os.path.basename(x))
    dir_list = sorted(dir_list, reverse=True)

    return dir_list