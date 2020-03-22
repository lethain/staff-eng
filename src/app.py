import os
import datetime
import feedgen.feed

from flask import Flask, render_template, make_response, request, redirect, abort
from stories import AUTHOR, get_stories, story_lookup
from index import chapters, section_lookup


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
    story_list = get_stories(ignore=app.debug)
    return [x for x in story_list if x.date() <= now_dt]

def next_story():
    now_dt = now()
    prev = None
    # no stories published
    story_list = get_stories(ignore=app.debug)

    if story_list[0].date() > now_dt:
        return story_list[0]

    for x in story_list:
        curr = x.date()
        if prev and prev < now_dt and curr >= now_dt:
            return x
        prev = curr

    if story_list[-1].date() > now_dt:
        return story_list[-1]


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
    details = story_lookup(name, ignore=app.debug)
    if details:
        return render_template("story.html", story=details)
    else:
        abort(404)


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
def guides():
    index = chapters()
    return render_template("guide.html", chapters=index['chapters'])

@app.route('/guide/<chapter>/<section>')
def guide(chapter, section):
    chapter, section = section_lookup(chapter, section)

    if section:
        return render_template("section.html", chapter=chapter, section=section)
    else:
        abort(404)


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
