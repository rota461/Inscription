import os

import jinja2
from pathlib import Path

from . import settings
from . import loader
from . import writer

# facade class

class Article(object):

    def __init__(self, content, datetime):
        self.content = content
        self.datetime = datetime
        
class Editor(object):
    def __init__(self, settings):
        self.settings = settings

    def write_blog(self):
        entries_dir = self.settings.PATH['entries'].replace('/', os.path.sep)
        template_dir = self.settings.PATH['templates'].replace('/', os.path.sep)
        
        template = self.settings.TEMPLATE['blog']

        entries_dir_list = loader.entries_dir_list(entries_dir)

        articles = []
        for entries_dir in entries_dir_list:
            md_list = loader.md_list(entries_dir, -1)    
            for md in md_list:
                content = writer.convert_md(md)
                datetime = os.path.basename(md)[:8]

                articles.append(Article(content, datetime))

        html = writer.write_blog(articles, template, template_dir)        

        return html

    def write_index(self):
        blog_dir = self.settings.PATH['entries']
        template_dir = self.settings.PATH['templates']

        template = self.settings.TEMPLATE['index']

        entries_dir_latest = loader.entries_dir_list(blog_dir)[0]

        articles = []
        md_list = loader.md_list(entries_dir_latest, 3)

        for md in md_list:
            content = writer.convert_md(md)
            datetime = os.path.basename(md)[:8]

            articles.append(Article(content, datetime))

        html = writer.write_blog(articles, template, template_dir)

        return html