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
    `mathjax` makes sure markdown doesn't ruin latex so that mathjax.js can render it.
    
    .. _FlatPages: http://packages.python.org/Flask-FlatPages/#flask_flatpages.pygmented_markdown
    .. _mathjax: https://github.com/mayoff/python-markdown-mathjax
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
    # Articles are pages with a publication date
    articles = (p for p in pages if 'date' in p.meta)
    # Show the 10 most recent articles, most recent first.
    articles = sorted(articles, reverse=True,
                    key=lambda p: p.meta['date'])
    return render_template('index.html', pages=articles)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

def freeze():
    freezer.freeze()

def serve_static():
    import os
    os.chdir("build")
    import SimpleHTTPServer, SocketServer
    PORT = 8000
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Serving static content from ",os.getcwd(),"at port", PORT
    print "Press Ctrl+C to interrupt"
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Server shutdown"
    
def serve_dynamic():
    app.run(port=8000)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "build":
            freeze()
        if sys.argv[1] == "static":
            freeze()
            serve_static()
        if sys.argv[1] == "serve":
            serve_dynamic()
