import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import inscription.loader

class TestLoader(object):

    def test_md_list(self):
        expected_all = ['20190213_3_test3.md','20190213_2_test2.md','20190213_1_test1.md']
        expected_top2 = ['20190213_3_test3.md','20190213_2_test2.md']

        chdir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(chdir,'contents/articles/').replace('/', os.path.sep)

        actual_all = inscription.loader.md_list(path, -1)
        actual_all = [os.path.basename(x) for x in actual_all]
        actual_top2 = inscription.loader.md_list(path, 2)
        actual_top2 = [os.path.basename(x) for x in actual_top2]
          
        assert actual_all == expected_all
        assert actual_top2 == expected_top2

    def test_entries_dir_list(self):
        expected = ['201903', '201902', '201901']

        chdir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(chdir, 'contents/entries/').replace('/', os.path.sep)
        
        actual = inscription.loader.entries_dir_list(path)
        actual = [os.path.basename(x) for x in actual]

        assert actual == expected