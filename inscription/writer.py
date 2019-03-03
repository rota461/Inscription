import os

import codecs
import jinja2
import markdown

from pathlib import Path

def convert_md(file):
    file = open(file, encoding='utf-8')
    text = file.read()

    mark = markdown.Markdown()
    md = mark.convert(text)

    file.close()
    return md

def write_blog(articles, template, template_path):
    loader = jinja2.FileSystemLoader(template_path)
    env = jinja2.Environment(
        loader = loader,
        autoescape = jinja2.select_autoescape(['html'])
    )
    template = env.get_template(template)

    return template.render(articles=articles)