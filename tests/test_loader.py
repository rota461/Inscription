import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from inscription.loader import Loader

class TestLoader(object):

    def test_md_list(self):
        expected = ['test1.md','test2.md','test3.md']
        loader = Loader()

        chdir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(chdir,'contents\\articles\\')

        actual = loader.md_list(path)

        assert actual == expected

    def test_template_list(self):
        expected = ['test1_template.html','test2_template.html','test3_template.html']
        loader = Loader()

        chdir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(chdir, 'templates\\')
        
        actual = loader.template_list(path)

        assert actual == expected