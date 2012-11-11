title: Citations in Markdown using Pandoc
datetime: 2012-10-12 15:35:00 +2
tags: [markdown, pandoc, citations, python]
category: [hacking,blog]

[TOC]

## Overview

[Pandoc](http://johnmacfarlane.net/pandoc/) is an amazing tool that can convert one markup language to another. 
It is very goot at parsing *Markdown* and it has the ability to parse [citations in *Markdown*](http://johnmacfarlane.net/pandoc/README.html#citations), 
which is exactly what I was looking for!

But I had some things to solve first.

## Problem 1

*Pandoc* didn't work with the <code>--bibliography</code> option (test using <code>pandoc -s -S --bibliography=references.bib test.md</code>)

## Solution 1

Change *Pandoc* version from _1.9.4.2a_ to _1.9.4.2_ (see [Install page](http://johnmacfarlane.net/pandoc/installing.html) - 
if you don't see the earlier version change from *Current downloads* to *All downloads* and hit *Search*.

## Problem 2

I want to run *Pandoc* from my *Python* site generator.
So I tried [pyandoc](http://pypi.python.org/pypi/pyandoc/).

Whenever I run the test *pyandoc*, though, I got an error that "Windows can't find the specified file".
I filed an [issue](https://github.com/kennethreitz/pyandoc/issues/5) and then found a solution.

## Solution 2

The path to the pandoc executable doesn't *really* change when setting it from *Python*,
so you got to change it in the original *pyandoc* file - <code>C:\\Python27\\Lib\\site-packages\\pandoc\\core.py</code>, 
and the code change is simply setting the <code>PANDOC_PATH</code> variable to the full path to your <code>pandoc.exe</code>.

## Problem 3

How to use pyandoc to parse my *Markdown* files?
Well, it looks pretty easy, writing a function that uses *pyandoc* and setting it 
at <code>sitebuilder.py</code>[^1] for the varialbe <code>FLATPAGES_HTML_RENDERER</code> that controls the renderer of pages.
But *pyandoc* doesn't use <code>--bibliography</code> and <code>--csl</code>!
 
## Solution 3

I forked *pyandoc* and added support for the <code>--bibliography</code> and <code>--csl</code> options. 
The code is on [GitHub](https://github.com/yoavram/pyandoc).

Also, I've written a new module for the site generator called *renderers* which has a factory function that creates a *Pandoc* renderer.
The *Pandoc* renderer uses my modified *pyandoc* to render *Markdown* text to *HTML*, including citations, math and everything.

This *Pandoc* renderer can be used as the <code>FLATPAGES_HTML_RENDERER</code> for [Flask-FlatPages](http://packages.python.org/Flask-FlatPages/#flask_flatpages)
on my <code>sitebuilder.py</code>.

The previous renderer was based on the default [Python-Markdown](http://freewisdom.org/projects/python-markdown/) with some extensions, so I had to find replacements for these extensions:

  - *MathJax* - just add <code>--mathjax</code> to the *Pandoc* call, using the <code>add_argument</code> method I added to <code>pyandoc.Document</code> in [#solution-3].
  - *Footnotes* - supported out-of-the-box by *Pandoc*. Just make sure to have an empty line before and after the footnotes definitions.
  - *Abbreviations* - not that important, so I deserted this feature
  - *Table of Contents* - a bit tricky. *Pandoc* uses the <code>--toc</code> option to generate a TOC. 
  I needed a way for the renderer to decide if a TOC was really desired. I decided that it will be added to posts that begin with [TOC],
  because that was sort-of the way the *Python-Markdown* TOC extension did it. So my renderer:
  -- looks for the <code>[TOC]</code> tag at the beginning of the post
  -- strips off the tag
  -- replaces it with an *HTML* <code>&lt;a name="TOC">&lt;/a></code> tag
  -- adds a *toc* argument via the <code>pyandoc.Document</code> class
  -- the TOC is inserted by *Pandoc* only if the <code>standalone</code> option is given or a suitable *template* is given, 
  so I created a template and gave it to *Pandoc* using the <code>add_argument</code> method:

<pre>
	$toc$
	$body$
</pre>

## Problem 4
 
How to get a real *bib* file? I use [Mendeley](http://www.mendeley.com/) to manage my references, 
so do I need to export the *bib* file from *Mendeley* each time I add a new document?

## Solution 4

No, as it happens, [Mendeley can sync to a bib file](http://blog.mendeley.com/tipstricks/how-to-series-generate-bibtex-files-for-your-collections-for-use-in-latex-part-3-of-12/).
This feature was designed for people writing papers with *LaTeX* but it is useful for me as well. So as long as I use *Mendeley*, I just need to point the 
renderer to the *bib* file I sync to *Mendeley* and that's it - this is done by giving the renderer factory a suitable argument <code>bib=/path/to/library.bib</code>.

CSL files are easier - just download the ones you want from [Zotero Style Repository](http://www.zotero.org/styles) and place the in the <code>sys.path</code> or in the <code>pandoc/csl</code> folder.

## Problem 5

As you can see in the [examples below](#examples), the references are not linked. 
Also it would be nice to create ciations by specifing a DOI and without a *bib* file, 
like it is down using [knitcitations in R](http://www.carlboettiger.info/2012/05/30/knitcitations.html).

But I'll leave that for another day.

## Examples

A few exmamples of how I write the *Markdown* and how it looks on the blog:

    ... in a process called *Muller's Ratchet* [@Muller1964; @Haigh1978].
	
... in a process called *Muller's Ratchet* [@Muller1964; @Haigh1978].


    .. as suggested by Drake [-@Drake1991].

.. as suggested by Drake [-@Drake1991].


    My model is based on that by @Hadany2003 who showed...

My model is based on that by @Hadany2003 who showed...

## References

[^1]: The main Python module underlying my [Python static site generator](https://github.com/yoavram/yoavram.github.com/tree/source)