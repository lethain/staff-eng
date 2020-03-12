import os
import feedgen.feed

from flask import Flask, render_template, make_response


class Story:
    def __init__(self, name, slug, date):
        self.name = name
        self.slug = slug
        self.date = date

STORIES = [
    Story("Keavy McMinn", "keavy-mcminn", "2020/3/1"),
]
        
    

app = Flask(__name__)

@app.route('/')
def front():
    return render_template("front.html")

@app.route('/stories')
def stories():
    return render_template("stories.html")

@app.route('/share')
def share():
    return render_template("share.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/stories/<name>')
def story(name):
    template_path = "stories/%s.html" % name
    return render_template(template_path)

@app.route('/rss')
def rss():
    fg = feedgen.feed.FeedGenerator()
    fg.title("StaffEng")
    fg.description("RSS feed for StaffEng.com")
    fg.author({'name': 'Will Larson', 'email': 'lethain@gmail.com'})
    fg.link(href='https://staffeng.com', rel='alternate')
    fg.link(href='https://staffeng.com/rss', rel='self')
    fg.language('en')

    txt =  fg.rss_str(pretty=True)
    resp = make_response(txt)
    resp.headers.set('Content-Type', 'application/rss+xml')
    return resp    


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

