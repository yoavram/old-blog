# -*- coding: utf-8 -*-
# https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/
import sys
import datetime
from renderers import pandoc_renderer
from flask import Flask, render_template, url_for, send_file, jsonify
# http://packages.python.org/Flask-FlatPages
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
WEBSITE_ADDRESS = "http://blog.yoavram.com"
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
GITHUB_USERNAME = u"yoavram"
MENDELEY_ID = u"yoav-ram"
GOOGLECODE_USERNAME = u"yoavram@gmail.com"
LINKEDIN_USERNAME = u"yoavram"
GOOGLE_SCHOLAR_CITATIONS_USER = u"RIFmJvYAAAAJ"
BIB_FILE = r'D:\library.bib'
CSL = "chicago"
LAST_MODIFICATION = datetime.datetime.now()
FIGSHARE_AUTHOR = "Yoav_Ram"
FIGSHARE_ID = "99206"
ORCID = "0000-0002-9653-4458"
FEED_URL = "http://feeds.feedburner.com/yoavram/msb-recent"
EMAIL_SUBSCRIPTION_URL = "http://feedburner.google.com/fb/a/mailverify?uri=yoavram/msb-recent"

FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_HTML_RENDERER = pandoc_renderer(bib=BIB_FILE, csl=CSL, math="mathjax", indented_code_classes=["prettyprint", "linenums:1"])
FLATPAGES_PDF_RENDERER = pandoc_renderer(target="pdf", template=None, bib=BIB_FILE, csl=CSL)

CATEGORIES = []

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


def add_bib_to_pages():
    import re
    citation_pattern = re.compile('@(\w+\d\d\d\d)', re.M)
    import sys
    sys.path.append(r"..\\..\\markx\\")
    import bibi
    bib = bibi.parse_file(app.config['BIB_FILE'])
    for p in pages:
        keys = set(citation_pattern.findall(p.body))
        p.bib = bibi.to_string(bib, keys).decode('utf-8')
add_bib_to_pages()

def load_categories(filename="categories.txt"):
    fin = open(filename)
    for category in fin:
        CATEGORIES.append(category)


# http://jinja.pocoo.org/docs/api/#custom-filters
def format_date(value, format="%B %d, %Y"):
    return value.strftime(format)


def format_datetime(value, format="%d %B %Y at %H:%M"):
    return value.strftime(format)


def format_time(value, format="%H:%M"):
    return value.strftime(format)

app.jinja_env.filters['format_datetime'] = format_datetime
app.jinja_env.filters['format_date'] = format_date
app.jinja_env.filters['format_time'] = format_time

## Generating ATOM feed
# http://flask.pocoo.org/snippets/10/
# http://werkzeug.pocoo.org/docs/contrib/atom/
from urlparse import urljoin
from werkzeug.contrib.atom import AtomFeed


def make_external(url):
    return urljoin(app.config['WEBSITE_ADDRESS'], url)


def permalink(page):
    return make_external(url_for("page", path=page.path))


def tag_count():
    tags = {}
    for p in pages:
        for t in p.meta.get('tags', []):
            tags[t] = tags.get(t, 0) + 1
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
    if (index + 1) < len(sorted_pages):
        return sorted_pages[index + 1]
    else:
        return None

app.jinja_env.globals['permalink'] = permalink
app.jinja_env.globals['make_external'] = make_external
app.jinja_env.globals['tag_count'] = tag_count
app.jinja_env.globals['prev_page'] = prev_page
app.jinja_env.globals['next_page'] = next_page
app.jinja_env.globals['sorted'] = sorted


@app.route('/recent.atom')
def recent_feed():
    articles = pages_by_datetime(15)
    feed = AtomFeed(u'Recent Articles',
                    feed_url=make_external(url_for("recent_feed")),
                    url=make_external(""),
                    author={'name': 'Yoav Ram', 'uri': 'http://www.yoavram.com/', 'email': 'yoavram@gmail.com'},
                    rights='CC BY-SA 3.0',
                    updated=articles[0].meta['datetime'])

    for article in articles:
        feed.add(article.meta['title'],
                 unicode(article.html),
                 content_type='html',
                 url=permalink(article),
                 updated=article.meta['datetime'])

    return feed.get_response()

## End of ATOM feed


def pages_by_datetime(limit=0, latest_first=True):
    # Articles are pages with a publication date
    articles = (p for p in pages if 'datetime' in p.meta)
    if not app.config['DEBUG']:
        articles = (a for a in articles if not 'draft' in a.meta)
    # Show the 10 most recent articles, most recent first.
    articles = sorted(articles, reverse=latest_first,
                    key=lambda p: p.meta['datetime'])
    if limit:
        return articles[:limit]
    else:
        return articles

def pages_by_category(articles):
    map = {}
    for p in articles:
        cats = p.meta.get('category', [])
        if len(cats)>0:
            c = cats[0]
        else:
            c = "uncategorized"
        if c in map:
            map[c].append(p)
        else:
            map[c] = [p]
    return map

@app.route('/')
def index():
    articles = pages_by_datetime()
    return render_template('index.html', pages=articles)


def page_to_pdf(page):
    text = page.body
    pdf = FLATPAGES_PDF_RENDERER(text, path=page.path, title=page.meta['title'], author=AUTHOR_FIRSTNAME+" "+AUTHOR_LASTNAME, date=page.meta['datetime'])
    return send_file(pdf)


@app.route('/orcid/')
def orcid():
    if ORCID:
        import orcid
        items = orcid.orcid_items(ORCID)    
    else:
        items = []
    return jsonify(data=items)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/pdf/<path:path>/')
def pdf(path):
    page = pages.get_or_404(path)
    return page_to_pdf(page)


@app.route('/tag/<string:tag>/')
def tag(tag):
    articles = pages_by_datetime()
    tagged = [p for p in articles if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


@app.route('/category/<string:category>/')
def category(category):
    articles = pages_by_datetime()
    categorized = [ p for p in articles if category in p.meta.get('category', [])]
    categories = [p.meta['category'] for p in categorized]
    subs = []
    for c in categories:
        ind = c.index(category)+1
        sub_cat = c[ind:]
        for s in sub_cat:
            if s not in subs:
                subs.append(s)
    subs.sort()
    return render_template('category.html', pages=categorized, category=category, subcategories=subs)

def freeze(debug=True):
    app.debug = debug
    freezer.freeze()


def serve_static():
    import os
    os.chdir("build")
    import SimpleHTTPServer
    import SocketServer
    PORT = 8000
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Serving static content from ", os.getcwd(), "at port", PORT
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
