import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from inscription.settings import Settings

class TestSettings(object):
    
    def test_read_config(self):
        settings = Settings()

        expected = "PATH"
        expected2 = "TEMPLATE"

        chdir = os.path.dirname(os.path.abspath(__file__))
        settings.read_config(chdir)

        actual = settings.PATH
        actual2 = settings.TEMPLATE
        
        assert actual['TEST'] == expected
        assert actual2['TEST'] == expected2