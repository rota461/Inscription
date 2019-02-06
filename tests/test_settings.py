import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from inscription.settings import Settings

class TestSettings(object):
    
    def test_read_config(self):
        settings = Settings()

        expected = "PASS"
        settings.read_config()
        actual = settings.PATH

        assert actual['TEST'] == expected

