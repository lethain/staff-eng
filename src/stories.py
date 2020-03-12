import datetime


AUTHOR = {'name': 'Will Larson', 'email': 'lethain@gmail.com'}

class Story:
    def __init__(self, name, role, slug, date_str, content):
        self.name = name
        self.role = role
        self.slug = slug
        self.date_str = date_str
        self.content = content

    def url(self):
        return "https://staffeng.com/stories/%s" % self.slug

    def title(self):
        return "%s - %s" % (self.name, self.role)

    def author(self):
        return AUTHOR

    def html(self):
        extra = "<p><a href=\"%s\">Read the full article on staffeng.com</a></p>"
        return self.content + extra

    def date(self):
        td = datetime.timedelta(hours=-7)
        tz = datetime.timezone(td)
        dt = datetime.datetime.strptime(self.date_str, "%Y-%m-%d %H")
        return dt.astimezone(tz=tz)


KEAVY_CONTENT = """
<p>
I'm a senior principal engineer at <a href="https://www.fastly.com/">Fastly</a>. Fastly is an edge cloud platform that provides services like a CDN. I work in OCTO, the Office of the CTO, which is composed of about ten principal or distinguished engineers who report directly to the CTO. Each member of OCTO tends to have their own focus, and mine is being the API Lead.
</p>
"""

    
STORIES = [
    Story("Keavy McMinn", "Senior Principal Engineer at Fastly", "keavy-mcminn", "2020-03-01 07", KEAVY_CONTENT),
]


