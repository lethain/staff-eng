import os

from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

