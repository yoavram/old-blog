title: Creating PDFs with Pandoc
datetime: 2012-12-16 11:36:00 +2
updated: 2012-12-18 12:10:00 +2
tags: [pdf, markdown, pandoc]
category: [hacking,blog]
math: true

[TOC]

## Overview

This post will show how to convert a [Markdown] document to PDF, mobile-PDF and EPUB documents using [Pandoc].
The guide is not exhastive but rather a walkthrough of my own experiments. The mobile-PDF especially is lacking - it is based on somewhat advanced $LaTeX$, and I'm a novice user of that language.

The source [Markdown] file use for this post, [creating-pdfs-with-pandoc.md], is available as a gist.

For more on rendering citations in [Markdown] with [Pandoc], see an [earlier post](/citations-in-markdown-using-pandoc/).

## Simple PDF rendering

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.pdf

[See result](https://www.box.com/s/sbsvcg28mnao4clscz5n)

## With bibliography

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.pdf --bibliography=<path to bibtex file> [--csl=<path to csl file>] [--toc]

The CSL file is optional, if ommited [Pandoc] uses [Chicago-style citations]. You can find more information on citation styles at <http://citationstyles.org/>. If you add the `--toc` option [Pandoc] will add a table of contents.

[See result](https://www.box.com/s/3ct61opmejh76nn374ri)

## Creating EPUB

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.epub --bibliography=<path to bibtex file> [--csl=<path to csl file>] [--toc]

On Windows 7 you can open EPUB files with [Calibre](http://calibre-ebook.com).

[See result](https://www.box.com/s/vaebc1h0l823yfqh1a3w)

## Creating PDFs for mobile phones

This is following the discussion on [tex.stackexchange](http://tex.stackexchange.com/questions/78920/generating-smartphone-readable-pdf), and using a [Pandoc] latex template which merges the default template with [this one](http://uweziegenhagen.de/?p=765). Here is [the template as a gist][iphone-pandoc-template.latex]. Remember to put the template in Pandoc's template folder (on Windows 7, C:\\Program Files (x86)\\Pandoc\\templates).

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.iphone.pdf -s --template=iphone-pandoc-template.latex --bibliography=<path to bibtex file> [--csl=<path to csl file>] [--toc]

This rendering is **not so good** - pages are split strangely and code segements are cropped. If anyone wants to play around with the [template][iphone-pandoc-template.latex], I'll be happy to post the results.

[See result](https://www.box.com/s/82kjkhck9nf87kfha9b0)

## Sample text with math, code and citation

Here is a reference [@Kimura1966], and also a link to my blog [Mutation-Selection Blog](http://blog.yoavram.com). Here's a footnote[^note] that you can see on the bottom.

One of my favorite mathematical expressions is the [triangle ineuqality](http://en.wikipedia.org/wiki/Triangle_inequality):

$$
\forall{x,y} \; \|x + y\| \leq \|x\| + \|y\|
$$

And a piece of Python code:

	for x in [p for p in posts if p['author'] == 'yoavram']:
		print x['date']
	print 'done'

## References

[^note]: Footnotes are great.

[Pandoc]: http://johnmacfarlane.net/pandoc/
[Markdown]: http://daringfireball.net/projects/markdown/
[iphone-pandoc-template.latex]: https://gist.github.com/3979276/
[creating-pdfs-with-pandoc.md]: https://gist.github.com/4305736/
[Chicago-style citations]: http://www.chicagomanualofstyle.org/tools_citationguide.html