# https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/
import sys

from flask import Flask, render_template, redirect, url_for
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
    .. _abbr: http://freewisdom.org/projects/python-markdown/Abbreviations
    .. _footnotes: http://freewisdom.org/projects/python-markdown/Footnotes
    .. _toc: http://freewisdom.org/projects/python-markdown/Table_of_Contents
    """
    extensions = ['mathjax', 'footnotes', 'abbr', 'toc']
    return markdown.markdown(text, extensions)

DEBUG = True
WEBSITE_ADDRESS = u"http://yoavram.bitbucket.org/"
BLOG_ADDRESS = WEBSITE_ADDRESS+u"blog"
SHARETHIS_PUBLISHER = "ur-fbcd7053-76f9-85c3-b29f-848f5f75e2af"
DISQUS_SHORTNAME = u"yoavram"
AUTHOR_LASTNAME = u"Ram"
AUTHOR_FIRSTNAME = u"Yoav"
AUTHOR_EMAIL = "yoavram@gmail.com"
BLOG_NAME = u"The Mutation-Selection Blog"
BLOG_MOTTO = u"Math, Science, Biology and the Mutation-Selection Balance"
GOOGLE_ANALYTICS = "UA-3865698-10"
AUTHOR_WEBSITE = u"http://www.yoavram.com/"
PUBMED_RSS = u"http://eutils.ncbi.nlm.nih.gov/entrez/eutils/erss.cgi?rss_guid=1RukBFKPvabUOwpqbC3ttHi8F4FuasZqQqkc1ePwc-qWGdC1Y8"
# https://twitter.com/settings/widgets/{{ config.TWITTER_WIDGET_ID }}/edit
TWITTER_USERNAME = u"yoavram"
TWITTER_WIDGET_ID = "253957912479793152"
FIGSHARE_ID = "99206"
BITBUCKET_USERNAME = u"yoavram"
MENDELEY_ID = u"yoav-ram"
GOOGLECODE_USERNAME = u"yoavram@gmail.com"
LINKEDIN_USERNAME = u"yoavram"
GOOGLE_SCHOLAR_CITATIONS_USER = u"RIFmJvYAAAAJ"

FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_HTML_RENDERER = pygmented_markdown

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# http://jinja.pocoo.org/docs/api/#custom-filters
def format_datetime(value, format="%B %d, %Y %Z"):
    return value.strftime(format)

app.jinja_env.filters['format_datetime'] = format_datetime


## Generating ATOM feed
# http://flask.pocoo.org/snippets/10/
# http://werkzeug.pocoo.org/docs/contrib/atom/
from urlparse import urljoin
from flask import request
from werkzeug.contrib.atom import AtomFeed

def make_external(url):
    return urljoin(request.url_root, url)

def tag_count():
    tags = {}
    for p in pages:
        for t in p.meta.get('tags', []):
            tags[t] = tags.get(t,0) + 1
    return tags

def prev_page(page):
    sorted_pages = pages_by_datetime(latest_first=False)
    index = sorted_pages.index(page)
    if index > 0:
        return sorted_pages[index - 1]
    else:
        return None

def next_page(page):
    sorted_pages = pages_by_datetime(latest_first=False)
    index = sorted_pages.index(page)
    if (index+1) < len(sorted_pages):
        return sorted_pages[index + 1]
    else:
        return None
    
app.jinja_env.globals['make_external'] = make_external
app.jinja_env.globals['tag_count'] = tag_count
app.jinja_env.globals['prev_page'] = prev_page
app.jinja_env.globals['next_page'] = next_page
app.jinja_env.globals['sorted'] = sorted

@app.route('/recent.atom')
def recent_feed():
    articles = pages_by_datetime(15)
    feed = AtomFeed(u'Recent Articles',
                    feed_url=request.url,
                    url=request.url_root,
                    author={'name':'Yoav Ram','uri':'http://www.yoavram.com/','email':'yoavram@gmail.com'},
                    rights='CC BY-SA 3.0',
                    updated=articles[0].meta['datetime'])
    
    for article in articles:
        feed.add(article.meta['title'],
                 unicode(article.html),
                 content_type='html',                 
                 url=make_external(article.path),
                 updated=article.meta['datetime'])
                 
    return feed.get_response()

## End of ATOM feed

def pages_by_datetime(limit=0, latest_first=True):
    # Articles are pages with a publication date
    articles = (p for p in pages if 'datetime' in p.meta)
    # Show the 10 most recent articles, most recent first.
    articles = sorted(articles, reverse=latest_first,
                    key=lambda p: p.meta['datetime'])
    if limit:
        return articles[:limit]
    else:
        return articles

@app.route('/')
def index():
    return redirect(url_for('blog'))

@app.route('/blog/')
def blog():
    articles = pages_by_datetime(10)
    return render_template('index.html', pages=articles)

@app.route('/blog/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/blog/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

def freeze(debug=True):
	app.config['DEBUG'] = debug
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
            freeze(False)
        if sys.argv[1] == "static":
            freeze()
            serve_static()
        if sys.argv[1] == "serve":
            serve_dynamic()
