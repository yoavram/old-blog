### MAIN FUNCTION ###
from os.path import exists
import re
citation_pattern = re.compile('@\w+\d\d\d\d')

''' Finds specified file in sys.path, <cwd>, <cwd>/pandoc, and returns the full path'''
def find_file_in_path(filename):
    import sys
    if exists(filename):
        return filename
    paths = ['pandoc','pandoc/csl']
    paths.extend(sys.path)
    for p in paths:
        if exists(p + '/' + filename):
            return p + '/' + filename
    raise IOError("File not found on path: %s" % filename)

def ensure_postfix(string, postfix):
    if string.endswith(postfix):
        return string
    else:
        return string + postfix

def pandoc_renderer(source = "markdown", target  = "html", bib = "references", csl = "chicago", template = "pandoc_template.txt", math = "mathjax", indented_code_classes=["prettyprint","linenums:1"]):    
    if source == "markdown" and target == "html":
        import pandoc
        bib = ensure_postfix(bib, '.bib')
        csl = ensure_postfix(csl, '.csl')        
        bib = find_file_in_path(bib)
        csl = find_file_in_path(csl)
        abbr = csl[:-4] + ".abbr"
        if not exists(abbr):
            abbr = None        
        template = find_file_in_path(template)
        
        def pandoc_markdown_html_renderer(text):      
            doc = pandoc.Document()
            if citation_pattern.search(text):
                # only use bib if there are citations,
                # because it takes longer to render due to large size of bib files
                doc.bib(bib)
                doc.csl(csl)
                if abbr:
                    doc.abbr(abbr)
            if text.startswith('[TOC]'):
                text = "<a name='TOC'></a>"+text[5:]
                doc.add_argument('toc')        
                doc.add_argument('template=%s' % template)
            if math:
                doc.add_argument(math)
            doc.add_argument('ascii') # to avoid "non-ascci" output bug
            if indented_code_classes:
                if isinstance(indented_code_classes, str):
                    doc.add_argument("indented-code-classes=%s" % indented_code_classes)
                elif isinstance(indented_code_classes, list):
                    doc.add_argument("indented-code-classes=%s" % ','.join(indented_code_classes))
            doc.markdown = text
            html = doc.html
            return unicode(html) # to catch "non-ascci" output bug
        return pandoc_markdown_html_renderer
    else:
        raise ValueError("No renderer for source %s and target %s" % (source, target))

### TEST CODE ###   
if __name__ == '__main__':
    def write(text,filename):
        fout = open(filename, 'wb')
        fout.write(p.html)
        fout.close()
        
    from flask import Flask
    from flask_flatpages import FlatPages
    #FLATPAGES_ROOT = "pages/"
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_HTML_RENDERER = pandoc_renderer(bib=r'd:\library.bib', csl="plos")
    app = Flask(__name__)
    app.config.from_object(__name__)
    pages = FlatPages(app)

    import os
    import os.path
    tmp_folder = "pandoc/tmp/"
    if not os.path.exists(tmp_folder):
        os.mkdir(tmp_folder)
   
    page_path = "pandoc-test"
    p=pages.get(page_path)
    write(p.html, tmp_folder+page_path+".html")

##    page_path = "blogging-with-math-and-code"
##    p=pages.get(page_path)
##    write(p.html, tmp_folder+page_path+".html")
##    
##    page_path = "markdown-links-and-footnotes"
##    p=pages.get(page_path)
##    write(p.html, tmp_folder+page_path+".html")


