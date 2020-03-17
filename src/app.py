import os
import datetime
import feedgen.feed

from flask import Flask, render_template, make_response, request, redirect
from stories import STORIES, AUTHOR
import yaml



app = Flask(__name__)

def now():
    td = datetime.timedelta(hours=-7)
    tz = datetime.timezone(td)

    override = request.args.get('date', None)
    if not override:
        dt = datetime.datetime.now()
    else:
        dt = datetime.datetime.strptime(override, "%Y-%m-%d")

    return dt.astimezone(tz=tz)

def published():
    now_dt = now()
    return [x for x in STORIES if x.date() <= now_dt]

def next_story():
    now_dt = now()
    prev = None
    # no stories published
    if STORIES[0].date() > now_dt:
        return STORIES[0]
    
    for x in STORIES:
        curr = x.date()
        if prev and prev < now_dt and curr >= now_dt:
            print("obviously yes")
            return x
        prev = curr

    if STORIES[-1].date() > now_dt:
        return STORIES[-1]


@app.route('/')
def front():
    story_list = list(reversed(published()[-3:]))
    nxt = next_story()
    return render_template("front.html", stories=story_list, next_story=nxt)

@app.route('/stories')
def stories():
    nxt = next_story()
    story_list = published()
    return render_template("stories.html", stories=story_list, next_story=nxt)

@app.route('/stories/<name>')
def story(name):
    template_path = "stories/%s.html" % name
    return render_template(template_path)

@app.route('/share')
def share():
    return render_template("share.html")

@app.route('/survey')
def survey():
    return redirect("https://airtable.com/shry1KXQCLWpnXuC5")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/guide')
def guide():
    with open("./src/chapters/index.yaml") as fin:
        index = yaml.load(fin.read())

    return render_template("guide.html", chapters=index['chapters'])

@app.route('/rss')
def rss():
    fg = feedgen.feed.FeedGenerator()
    fg.id("https://staffeng.com/")
    fg.title("StaffEng")
    fg.description("RSS feed for StaffEng.com")
    fg.author(AUTHOR)
    fg.link(href='https://staffeng.com', rel='alternate')
    fg.link(href='https://staffeng.com/rss', rel='self')
    fg.language('en')
    fg.updated(now())

    for story in published()[-10:]:
        fe = fg.add_entry()
        fe.id(story.url())
        fe.title(story.title())
        fe.link(href=story.url(), rel="alternate")
        fe.published(story.date())
        fe.updated(updated=story.date())
        fe.author(AUTHOR)
        fe.content(content=story.html(), type="CDATA")

    txt =  fg.rss_str(pretty=True)
    resp = make_response(txt)
    resp.headers.set('Content-Type', 'application/rss+xml')
    return resp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
