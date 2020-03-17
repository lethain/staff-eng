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
    Story("Keavy McMinn", "Senior Principal Engineer at Fastly", "keavy-mcminn", "2020-03-24 03", KEAVY_CONTENT),
    Story("Dan Na", "Staff Engineer and Team Lead at Squarespace", "dan-na", "2020-03-26 03", DAN_NA_CONTENT),
    Story("Joy Ebertz", "Senior Staff Software Engineer at Split", "joy-ebertz", "2020-03-31 03", JOY_EBERTZ_CONTENT),
    Story("Ritu Vincent", "Staff Engineer at Dropbox", "ritu-vincent", "2020-04-02 03", RITU_VINCENT_CONTENT),
    Story("Nelson Elhage", "Formerly Staff Engineer at Stripe", "nelson-elhage", "2020-04-07 03", NELHAGE_CONTENT),
    # 6. silvia 04-09
    # 7. rick 04-14
    # 8. duretti 04-16
    Story("Diana Pojar", "Staff Data Engineer at Slack", "diana-pojar", "2020-04-21 03", DIANA_POJAR_CONTENT),
    # 10. michelle 04-23
]
