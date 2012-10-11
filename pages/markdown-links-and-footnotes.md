title: Markdown links and footnotes
datetime: 2012-10-11 11:21:00 +2
tags: [blog, markdown]

Following are examples of how to do links, footnotes and abbreviations in [Markdown](http://daringfireball.net/projects/markdown/).

### Contents

[TOC]

### [Links](http://daringfireball.net/projects/markdown/syntax#link)

Links can be written in several ways:

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

### [Footnotes](http://freewisdom.org/projects/python-markdown/Footnotes)

<pre>
You can see a footnote here[^here].
</pre>
Also, you can see a footnote here[^here].

Click on the little *1* to see the footnote.
Again, you'll need to put this somewhere, usually at the bottom:

<pre>
[^here]: This a footnote, it leads to [somewhere] but not much *else*.
</pre>

###[Abbreviations](http://freewisdom.org/projects/python-markdown/Abbreviations)

<pre>
You can also do abbreviations, like MSB or NBA.
</pre>
You can also do abbreviations, like MSB or NBA.
Point at an abbreviation to see it expand.ss
And stick these wherever:

<pre>
*[NBA]: National Basketball Association
*[MSB]: Mutation-Selection Balance
</pre>

[somewhere]: http://somewhere.com "Somewhere"
[1]: http://neverwhere.com/
[^here]: This a footnote, it leads to [somewhere] but not much *else*.

*[NBA]: National Basketball Association
*[MSB]: Mutation-Selection Balance
