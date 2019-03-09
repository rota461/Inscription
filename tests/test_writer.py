import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from inscription import writer
from inscription.editor import Article

class TestWriter(object):

    def test_convert_md(self):
        expected = '<h1>test</h1>'
        
        chdir = os.path.dirname(os.path.abspath(__file__))
        file = 'contents/articles/20190213_1_test1.md'.replace('/',os.path.sep)
        file_path = os.path.join(chdir, file)
        
        actual = writer.convert_md(file_path)

        assert actual == expected

    def test_write_blog(self):
        expected = '<span>2019/02/01</span>\n<h1>Test1</h1>\n<p>test</p>\n<span>2019/02/02</span>\n<h1>Test2</h1>\n<p>test</p>\n'

        chdir = os.path.dirname(os.path.abspath(__file__))
        templates_path = os.path.join(chdir, 'templates')
        template = 'test1_template.html'

        articles = []
        article1 = Article('<h1>Test1</h1>\n<p>test</p>', '2019/02/01')
        article2 = Article('<h1>Test2</h1>\n<p>test</p>', '2019/02/02')

        articles.append(article1)
        articles.append(article2)

        actual = writer.write_blog(articles,template, templates_path)

        assert actual == expected