import os

from inscription.editor import Editor
from inscription.settings import Settings

if __name__ == "__main__":
    settings = Settings()
    settings.read_config(settings.cdir)
    
    editor = Editor(settings)

    blog = editor.write_blog()
    index = editor.write_index()

    file = open(settings.PATH['outputs'] + 'index.html', 'w+')
    file.write(index)
    file.close()

    file = open(settings.PATH['outputs'] + 'blog.html', 'w+')
    file.write(blog)
    file.close()
