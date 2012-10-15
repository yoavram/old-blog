title: Blogging with math and code
datetime: 2012-10-03 15:05:00 +2
tags: [blog, latex, markdown]
math: true

[TOC]

## Examples

### LaTeX

When $a \ne 0$, there are two solutions to $ax^2 + bx + c = 0$ and they are 
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
$$

### Source Code

#### Java

<pre class="prettyprint">
class Voila {
public:
  // Voila
  static const string VOILA = "Voila";
}
</pre>

#### Python

<pre class="prettyprint linenums:1">
      #!/usr/bin/python
      """
      xml2html: Convert XML to HTML
      
      *** SUPERSEDED by pyslt ***
      
      Uses SAX (event-based parsing).
      
      ***LICENSE***
      """
      
      _ID = '$Id: xml2html-1.01-1.py,v 1.1.1.1 2000/01/15 14:37:46 ecoaccess Exp $'
      
      import sys, copy
      from xml.sax.drivers.drv_xmlproc_val import *
      
      class myParser(SAX_XPValParser):
          """XML parser."""
      
          psl = None
      
          def handle_doctype(self, rootname, pub_id, sys_id):
              self.dtd_handler.doctypeDecl(rootname, pub_id, sys_id, self.psl)
</pre>

#### Inline code

Small code elements like <code>print 'Hello World!'</code> can be put into HTML <code>&lt;code></code> elements.

## Explanations

### LaTeX

$LaTeX$[^latex] is written inside the [Markdown](http://daringfireball.net/projects/markdown/)[^markdown] text using <code>&#36;</code> (once for inline, two for display mode).
Markdown identifies this is LaTeX because of the Python-Markdown extension [Markdown-MathJax](https://github.com/mayoff/python-markdown-mathjax). The LaTeX is then converted to mathematical notation in the browser using [MathJax](http://www.mathjax.org) javascript. 
To use it, you put the following in the <code><head\></code> of your HTML file:

<pre class="prettyprint html">
	&lt;script type="text/x-mathjax-config">
	  MathJax.Hub.Config({
				"tex2jax": { inlineMath: [ [ '$', '$' ] ] },
				"HTML-CSS": { availableFonts: ["STIX", "TeX"], 
							  linebreaks: { automatic: true }
				}
	  });
	&lt;/script>
	&lt;script type="text/javascript"
	  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML">
	&lt;/script>
	
</pre>

The confguration parameters are as follows:

  - <code>inlineMath</code> tells the MathJax script to use dollar signs for inline math.
  - <code>availableFonts</code> tells it to prefer using the [STIX](http://www.stixfonts.org/) font if it is available.
  - <code>linebreaks</code> tells it to automatically break (wrap) long equations.
  
Now you can write: <code>$LaTeX$ is cool:
$$
p' = p + (1-p)(1-s)\mu
$$</code>
to get the following result:

$LaTeX$ is cool:
$$
p' = p + (1-p)(1-s)\mu
$$


For more information visit the [documentation](http://docs.mathjax.org/en/latest/output.html)[^mathjax-debug].

### Source Code 

Code is writeen in the [Markdown](http://daringfireball.net/projects/markdown/) text by wrapping it with <code>&lt;pre class="prettyprint html">...&lt;/pre></code> element.
It is then highlighted in the browser using [Google code prettifier](http://google-code-prettify.googlecode.com) javascript which automatically identifies the language. 

See the [README](http://google-code-prettify.googlecode.com/svn/trunk/README.html) for detailed instructions. 
It's very easy to use and is the highligher used by [Google Code](http://code.google.com) and [stackoverflow.com](http://stackoverflow.com/).

If you have problems displaying HTML or XML source I suggest trying to replace <code>&lt;</code> with <code>&amp;lt;</code>[^html-escaping-tool].

For a nice example of different styles you can use (by replacing the default <code>prettify.css</code> file), see [Stanley Ng's website](http://demo.stanleyhlng.com/prettify-js/?id=sons-of-obsidian-dark).


[^latex]: [Online LaTeX editor](http://texify.com/)
[^markdown]: [Online Markdown editor](http://www.ctrlshift.net/project/markdowneditor/)
[^html-escaping-tool]: [Online HTML escaping tool](http://www.htmlescape.net/htmlescape_tool.html)
[^mathjax-debug]: [Online MathJax debugger](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).