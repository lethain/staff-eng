import datetime
from content import *


AUTHOR = {'name': 'Will Larson', 'email': 'lethain@gmail.com'}

class Story:
    def __init__(self, name, role, slug, date_str, content):
        self.name = name
        self.role = role
        self.slug = slug
        self.date_str = date_str
        self.content = content

    def local_url(self):
        return "/stories/%s" % self.slug

    def url(self):
        return "https://staffeng.com/stories/%s" % self.slug

    def title(self):
        return "%s - %s" % (self.name, self.role)

    def author(self):
        return AUTHOR

    def html(self):
        extra = "<p><a href=\"%s\">Read the full article on staffeng.com</a></p>" % (self.url())
        return self.content + extra

    def date(self):
        td = datetime.timedelta(hours=-7)
        tz = datetime.timezone(td)
        dt = datetime.datetime.strptime(self.date_str, "%Y-%m-%d %H")
        return dt.astimezone(tz=tz)


STORIES = [
    Story("Keavy McMinn", "Senior Principal Engineer at Fastly", "keavy-mcminn", "2020-03-24 07", KEAVY_CONTENT),
    Story("Dan Na", "Staff Engineer and Team Lead at Squarespace", "dan-na", "2020-03-26 07", DAN_NA_CONTENT),
    Story("Joy Ebertz", "Senior Staff Software Engineer at Split", "joy-ebertz", "2020-03-31 07", JOY_EBERTZ_CONTENT),
    Story("Ritu Vincent", "Staff Engineer at Dropbox", "ritu-vincent", "2020-05-02 07", RITU_VINCENT_CONTENT),
    Story("Nelson Elhage", "Formerly Staff Engineer at Stripe", "nelson-elhage", "2020-04-07 07", NELHAGE_CONTENT),
    # 6. silvia
    # 7. rick
    # 8. duretti
    # 9. dianna
    # 10. michelle
]
