import datetime
import markdown
import yaml
from flask import Markup
from content import *


AUTHOR = {'name': 'Will Larson', 'email': 'lethain@gmail.com'}


class Story:
    def __init__(self, name, role, slug, date_str, content):
        self.name = name
        self.role = role
        self.slug = slug
        self.date_str = date_str
        self.content = content
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
        extra = "<p><a href=\"%s\">Read the full article on staffeng.com</a></p>" % (self.url())
        return self.content + extra

    def date(self):
        td = datetime.timedelta(hours=-7)
        tz = datetime.timezone(td)
        dt = datetime.datetime.strptime(self.date_str, "%Y-%m-%d %H")
        return dt.astimezone(tz=tz)



STORIES_CACHE = None

def stories():
    global STORIES_CACHE
    if not STORIES_CACHE:
        with open("./src/stories/index.yaml") as fin:
            story_data = yaml.load(fin.read(), Loader=yaml.FullLoader)
        STORIES_CACHE = [Story(x['name'], x['title'], x['slug'], x['date'], '') for x in story_data['stories']]
    return STORIES_CACHE


def add_markdown(story):
    if not story.markdown:
        with open("./src/stories/%s.md" % (story.slug,), 'r') as fin:
            raw = fin.read()
            story.markdown = Markup(markdown.markdown(raw))
            


def story_lookup(slug):
    story_list = stories()
    for story in story_list:
        if story.slug == slug:
            add_markdown(story)
            return story
        

STORIES = [
    Story("Keavy McMinn", "Senior Principal Engineer at Fastly", "keavy-mcminn", "2020-03-24 07", KEAVY_CONTENT),
    Story("Dan Na", "Staff Engineer and Team Lead at Squarespace", "dan-na", "2020-03-26 07", DAN_NA_CONTENT),
    Story("Joy Ebertz", "Senior Staff Software Engineer at Split", "joy-ebertz", "2020-03-31 07", JOY_EBERTZ_CONTENT),
    Story("Ritu Vincent", "Staff Engineer at Dropbox", "ritu-vincent", "2020-04-02 07", RITU_VINCENT_CONTENT),
    Story("Nelson Elhage", "Formerly Staff Engineer at Stripe", "nelson-elhage", "2020-04-07 07", NELHAGE_CONTENT),
    # 6. silvia 04-09
    # 7. rick 04-14
    # 8. duretti 04-16
    Story("Diana Pojar", "Staff Data Engineer at Slack", "diana-pojar", "2020-04-21 07", DIANA_POJAR_CONTENT),
    # 10. michelle 04-23
]

STORIES = stories()
