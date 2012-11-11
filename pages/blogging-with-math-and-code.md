title: Blogging with math and code
datetime: 2012-10-03 15:05:00 +2
tags: [latex, markdown]
category: [hacking, blog]
math: true
updated: 2012-10-21 21:50:00 +2

[TOC]

## Examples

### Math

When $a \ne 0$, there are two solutions to $ax^2 + bx + c = 0$ and they are 
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}.
$$

### Source Code

#### Java

	class Blog {
	public:
	  // Blog
	  static const string BLOG = "Blog";
	}

#### Python

    #!/usr/bin/python
    def pages_by_datetime(limit=0, latest_first=True):
		# Articles are pages with a publication date
		articles = (p for p in pages if 'datetime' in p.meta)

		# Show the 10 most recent articles, most recent first.
		articles = sorted(articles, reverse=latest_first, key=lambda p: p.meta['datetime'])
		if limit:
			return articles[:limit]
		else:
			return articles

#### Inline code

Small code elements like <code>print 'Hello World!'</code> can be put into HTML <code>&lt;code></code> elements.

## Explanations

### Math

Math is written in $LaTeX$[^latex] is written inside the [Markdown][^markdown] text using <code>&#36;</code> 
(once for inline, two for display mode).
[Pandoc], which is used to convert the [Markdown] to HTML, is informed that $LaTeX$ 
is to be converted to mathematical notation in the browser using [MathJax] javascript by specifing the command line argument
<code>--mathjax</code>. [Pandoc] then converts <code>&#36;</code> to <code>\(</code> or <code>\)</code> to start and finish $LaTeX$ blocks and
doesn't parse [Markdown] inside these blocks.

To enable [MathJax], you put the following in the <code><head\></code> of your HTML file:

	<script type="text/x-mathjax-config">
	  MathJax.Hub.Config({
				"HTML-CSS": { availableFonts: ["STIX", "TeX"], 
							  linebreaks: { automatic: true }
				}
	  });
	</script>
	<script type="text/javascript"
	  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML">
	</script>

The confguration parameters are as follows:

  - <code>availableFonts</code> tells it to prefer using the [STIX](http://www.stixfonts.org/) font if it is available.
  - <code>linebreaks</code> tells it to automatically break (wrap) long equations.
  
Now you can write:
<pre>
	$LaTeX$ is cool:
	$$
	p' = p + (1-p)(1-s)\mu
	$$
</pre>
	
to get the following result:

$LaTeX$ is cool:
$$
p' = p + (1-p)(1-s)\mu
$$


For more information visit the [documentation](http://docs.mathjax.org/en/latest/output.html)[^mathjax-debug].

### Source Code 

Code is written inside the [Markdown] markup language by indenting it with a tab or four space.
The [Markdown] is converted to HTML with [Pandoc], which recognized these indented lines and wraps them with a <code>&lt;pre></code> element.
The CSS class given to the <code>&lt;pre></code> element is set to <code>prettyprint</code>, which is 
then highlighted in the browser using [Google code prettifier] javascript which automatically 
identifies the language. The CSS class is actually <code>prettyprint linenum:1</code> which tells the highlighter to number the lines.

See the [Pandoc handbook](http://johnmacfarlane.net/pandoc/README.html#indented-code-blocks) for instructions on the indented code blocks and the
code prettifier [README](http://google-code-prettify.googlecode.com/svn/trunk/README.html) for detailed instructions on the highlighting mechanism.
It's very easy to use and is the highligher used by [Google Code](http://code.google.com) and [stackoverflow.com](http://stackoverflow.com/).

If you have problems displaying HTML or XML source I suggest trying to replace <code>&lt;</code> with <code>&amp;lt;</code>[^html-escaping-tool].

For a nice example of different highlighting styles you can use (by replacing the default <code>prettify.css</code> file), see [Stanley Ng's website](http://demo.stanleyhlng.com/prettify-js/?id=sons-of-obsidian-dark).

[Markdown]: http://daringfireball.net/projects/markdown/
[MathJax]: http://www.mathjax.org/
[Pandoc]: http://johnmacfarlane.net/pandoc/
[Google code prettifier]: http://google-code-prettify.googlecode.com/

[^latex]: [Online LaTeX editor](http://texify.com/)
[^markdown]: [Online Markdown editor](http://www.ctrlshift.net/project/markdowneditor/)
[^html-escaping-tool]: [Online HTML escaping tool](http://www.htmlescape.net/htmlescape_tool.html)
[^mathjax-debug]: [Online MathJax debugger](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).