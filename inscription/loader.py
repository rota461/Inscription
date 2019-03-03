import os
import glob
from pathlib import Path

def md_list(path, count):
    path = Path(path)
    # entries or articles name must be yyyymmdd_serial_title.md.
    md_list = path.glob('*_*_*.md')
    md_list = sorted(md_list, reverse=True)

    if count == -1:
        return md_list
    else :
        return md_list[0:count]

def entries_dir_list(path):
    path = Path(path)
    tmp_list = path.glob('*')
    dir_list = []

    for x in tmp_list:
        if os.path.isdir(x):
            dir_list.append(x)
    dir_list = sorted(dir_list, reverse=True)

    return dir_list