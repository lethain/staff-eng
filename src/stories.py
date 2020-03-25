import datetime
import markdown
import yaml
from flask import Markup


STORIES_CACHE = None
AUTHOR = {'name': 'Will Larson', 'email': 'lethain@gmail.com'}


class Story:
    def __init__(self, name, role, slug, date_str):
        self.name = name
        self.role = role
        self.slug = slug
        self.date_str = date_str
        self.markdown = ""

    def local_url(self):
        return "/stories/%s" % self.slug

    def url(self):
        return "https://staffeng.com/stories/%s" % self.slug

    def title(self):
        return "%s - %s" % (self.name, self.role)

    def author(self):
        return AUTHOR

    def html(self):
        "Only used for RSS."
        if not self.markdown:
            add_markdown(self)

        title = Markup("<h1>%s</h1>" % (self.title(),))
        extra = Markup("<p><a href=\"%s\">Read the full article on staffeng.com</a></p>" % (self.url()))
        return extra + title + self.markdown

    def date(self):
        td = datetime.timedelta(hours=-7)
        tz = datetime.timezone(td)
        dt = datetime.datetime.strptime(self.date_str, "%Y-%m-%d %H")
        return dt.astimezone(tz=tz)


def get_stories(ignore=False):
    global STORIES_CACHE
    if not STORIES_CACHE or ignore:
        with open("./src/stories/index.yaml") as fin:
            story_data = yaml.load(fin.read(), Loader=yaml.FullLoader)
        STORIES_CACHE = [Story(x['name'], x['title'], x['slug'], x['date']) for x in story_data['stories']]
    return STORIES_CACHE


def add_markdown(story):
    if not story.markdown:
        with open("./src/stories/%s.md" % (story.slug,), 'r') as fin:
            raw = fin.read()
            story.markdown = Markup(markdown.markdown(raw))


def story_lookup(slug, ignore=False):
    story_list = get_stories(ignore=ignore)
    for story in story_list:
        if story.slug == slug:
            add_markdown(story)
            return story
