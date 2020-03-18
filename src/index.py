import yaml
import markdown
from flask import Markup


CHAPTER_CACHE = None


def chapters():
    global CHAPTER_CACHE
    if not CHAPTER_CACHE:
        with open("./src/chapters/index.yaml") as fin:
            CHAPTER_CACHE = yaml.load(fin.read(), Loader=yaml.FullLoader)
    return CHAPTER_CACHE


def add_markdown(section):
    if 'markdown' not in section:
        with open("./src/chapters/%s.md" % (section['slug'],), 'r') as fin:
            raw = fin.read()
            rendered = markdown.markdown(raw)
            section['markdown'] = Markup(rendered)
    

def section_lookup(chapter_slug, section_slug):
    index = chapters()
    for chapter in index['chapters']:
        if 'slug' in chapter and chapter['slug'] == chapter_slug:
            for section in chapter['sections']:
                if 'slug' in section and section['slug'] == section_slug:
                    add_markdown(section)
                    return chapter, section
    return None, None

    
