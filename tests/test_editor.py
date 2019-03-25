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

    def test_write_entries(self):
        chdir = os.path.dirname(os.path.abspath(__file__))

        html_expected1 = '<span>20190215</span><h1>test3</h1>'
        html_expected2 = '<span>20190214</span><h1>test2</h1>'
        html_expected3 = '<span>20190213</span><h1>test</h1>'

        serial_expected1 = '20190215003'
        serial_expected2 = '20190214002'
        serial_expected3 = '20190213001'
        
        settings = Settings()
        settings.read_config(chdir)

        editor = inscription.editor.Editor(settings)

        html_list, serial_list = editor.write_entry_pages()

        html_actual1 = html_list[0]
        html_actual2 = html_list[1]
        html_actual3 = html_list[2]

        serial_actual1 = serial_list[0]
        serial_actual2 = serial_list[1]
        serial_actual3 = serial_list[2]

        assert html_expected1 == html_actual1
        assert html_expected2 == html_actual2
        assert html_expected3 == html_actual3
        assert serial_expected1 == serial_actual1
        assert serial_expected2 == serial_actual2
        assert serial_expected3 == serial_actual3