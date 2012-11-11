title: Markdown links and footnotes
datetime: 2012-10-11 11:21:00 +2
tags: [markdown]
category: [hacking,blog]

[TOC]

Following are examples of how to do links and footnotes in [Markdown](http://daringfireball.net/projects/markdown/).

### Links

[Links](http://daringfireball.net/projects/markdown/syntax#link) can be written in several ways:

#### Inline

<pre>
Here is a link to [my website](http://www.yoavram.com).
</pre>
Here is a link to [my website](http://www.yoavram.com).

#### Reference

<pre>
Now you can see a link to [somewhere], and another to [neverwhere][1].
</pre>
Now you can see a link to [somewhere], and another to [neverwhere][1].

Try the tooltip on *somehwere*.

Make sure you stick these reference at the bottom, or wherever you want:

<pre>
[somewhere]: http://somewhere.com "Somewhere"
[1]: http://neverwhere.com/
</pre>

#### Automatic

<pre>
There are also automatic links, see &lt;http://daringfireball.net/projects/markdown/syntax#autolink>
</pre>
There are also automatic links, see <http://daringfireball.net/projects/markdown/syntax#autolink>

### Footnotes

[Footnotes](http://freewisdom.org/projects/python-markdown/Footnotes) are useful:

<pre>
You can see a footnote here[^here].
</pre>
You can see a footnote here[^here].

Click on the little *1* to see the footnote.
Again, you'll need to put this somewhere, usually at the bottom:

<pre>
[^here]: This a footnote, it leads to [somewhere] but not much *else*
</pre>

[somewhere]: http://somewhere.com "Somewhere"
[1]: http://neverwhere.com/

[^here]: This a footnote, it leads to [somewhere] but not much *else*
