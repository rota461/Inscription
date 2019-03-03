import os
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import inscription.editor
from inscription.settings import Settings

class TestEditor(object):

    def test_write_blog(self):
        chdir = os.path.dirname(os.path.abspath(__file__))

        expected = textwrap.dedent('''\
            <span>20190215</span>
            <h1>test3</h1>
            <span>20190214</span>
            <h1>test2</h1>
            <span>20190213</span>
            <h1>test</h1>
        ''')

        settings = Settings()
        settings.read_config(chdir)
        
        editor = inscription.editor.Editor(settings)
        
        actual = editor.write_blog()

        assert actual == expected

    def test_write_index(self):
        chdir = os.path.dirname(os.path.abspath(__file__))

        expected = textwrap.dedent('''\
            <span>20190215</span>
            <h1>test3</h1>
            <span>20190214</span>
            <h1>test2</h1>
            <span>20190213</span>
            <h1>test</h1>
        ''')

        settings = Settings()
        settings.read_config(chdir)
        
        editor = inscription.editor.Editor(settings)
        
        actual = editor.write_index()

        assert actual == expected