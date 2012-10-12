### MAIN FUNCTION ###

def pandoc_renderer(source = "markdown", target  = "html", bib = "references", csl = "chicago", template = "pandoc_template.txt", math = "mathjax"):    
    if source == "markdown" and target == "html":
        import pandoc
        def pandoc_markdown_html_renderer(text):      
            doc = pandoc.Document()
            doc.bib('pandoc/%s.bib' % bib)
            doc.csl('pandoc/csl/%s.csl' % csl)
            if text.startswith('[TOC]'):
                text = "<a name='TOC'></a>"+text[5:]
                doc.add_argument('toc')        
                doc.add_argument('template=pandoc/%s' % template)
            if math:
                doc.add_argument(math)
            doc.add_argument('ascii') # to avoid "non-ascci" output bug
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
    FLATPAGES_HTML_RENDERER = pandoc_renderer(csl="plos")
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


