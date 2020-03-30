import yaml
import markdown
from flask import Markup


CHAPTER_CACHE = None


def get_chapters(ignore=False):
    global CHAPTER_CACHE
    if not CHAPTER_CACHE or ignore:
        with open("./src/chapters/index.yaml") as fin:
            CHAPTER_CACHE = yaml.load(fin.read(), Loader=yaml.FullLoader)
    return CHAPTER_CACHE


def add_markdown(section):
    if 'markdown' not in section:
        with open("./src/chapters/%s.md" % (section['slug'],), 'r') as fin:
            raw = fin.read()
            rendered = markdown.markdown(raw)
            section['markdown'] = Markup(rendered)


def section_lookup(section_slug, ignore=False):
    index = get_chapters(ignore=ignore)
    for chapter in index['chapters']:
        curr_section = None
        prev_section = None
        sections = chapter['sections']
        with_next = zip(sections, sections[1:] + [None])
        for section, next_section in with_next:
            if 'slug' in section and section['slug'] == section_slug:
                add_markdown(section)
                section['prev'] = prev_section if prev_section and 'slug' in prev_section else None
                section['next'] = next_section if next_section and 'slug' in next_section else None
                return chapter, section
            prev_section = section
    return None, None
