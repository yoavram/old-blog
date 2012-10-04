# https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/
import sys

from flask import Flask, render_template
# http://packages.python.org/Flask-FlatPages
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
import markdown

def pygmented_markdown(text):
    """
    Added extensions to the default `FlatPages` renderer.
    
    .. _FlatPages: http://packages.python.org/Flask-FlatPages/#flask_flatpages.pygmented_markdown
    """
    try:
        import pygments
    except ImportError:
        extensions = []
    else:
        extensions = ['codehilite', 'mathjax']
    return markdown.markdown(text, extensions)


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_HTML_RENDERER = pygmented_markdown

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        # go to build folder and run "> python -m SimpleHTTPServer"
    else:
        app.run(port=8000)
