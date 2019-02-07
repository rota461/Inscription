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