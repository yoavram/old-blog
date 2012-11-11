title: Creating PDFs with Pandoc
datetime: 2012-10-20 10:41:00 +2
tags: [pdf, markdown]
category: [hacking,blog]
draft: true

[TOC]

## Simple PDF rendering

The source is in Markdown.

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.pdf

## With bibliography

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.pdf --bibliography=<path to bibtex file> [--csl=<path to csl file>]

The CSL file is optional, if ommited Pandoc uses Chicago CSL.

## Creating EPUB

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.epub --bibliography=d:\library.bib

On Windows 7 you can open EPUB files with [Calibre](http://calibre-ebook.com).

## Creating PDFs for mobile phones

This is following the discussion on [tex.stackexchange](http://tex.stackexchange.com/questions/78920/generating-smartphone-readable-pdf), and using a Pandoc latex template which merges the default template with [this one](http://uweziegenhagen.de/?p=765). Here is the [source as a gist](https://gist.github.com/3979276).

The command is:

	> pandoc creating-pdfs-with-pandoc.md -o creating-pdfs-with-pandoc.tex -s --template=iphone.latex

Of course you can add the <code>--bibliography</code>, as above.

This rendering is not that good - pages are split strangely and code segements are cropped.

## Plans

  - Make the mobile output better
  - Incorporate this commands to my blog framework to provide PDF/ePUB/mobile-PDF
  - Check out [pander](http://rapporter.github.com/pander/)

## Some sample text to see how it renders

Here is a reference [@Kimura1966], and also a link to my blog [Mutation-Selection Blog](http://blog.yoavram.com). Here's a footnote[^note] that you can see on the bottom.

One of my favorite mathematical expressions is the [triangle ineuqality](http://en.wikipedia.org/wiki/Triangle_inequality):
$$
\forall{x,y} \; \|x + y\| \leq \|x\| + \|y\|
$$

## References

[^note]: How nice to write footnotes.