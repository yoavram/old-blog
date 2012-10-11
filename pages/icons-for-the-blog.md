title: Icons for the blog
datetime: 2012-10-11 16:59:00 +2
tags: [blog]

### The problem
To build this blog I used the wonderful [Twitter Bootstrap] framework. 
It's hard to define what it is, so I'll leave it for another time.
*Twitter Bootstrap* comes packed with 120 icons packaged under the name [Glyphicons] *Halflings*. 
These are a subset of the *Glyphicons Free* set, and they include most of the little icons you see around the blog,
like:

  - the user icon: <i class="icon-user"></i>
  - the time icon: <i class="icon-time"></i> 
  - the tag icon: <i class="icon-tag"></i>
  
For a complete list visit either *Glyphicons* or [Twitter Bootstrap icons documentation]

But when I built the top navigation bar, I saw that I needed something more - I needed a button for my [web feed].
Web feeds (or RSS) have distinctive icons, but the *Glyphicons Halflings* set didn't have the feed\RSS icon.
But there is an RSS icon in *Glyphicons Free* - here it is <i class="glyphicon-rss"></i>. 

So how do I add it to my site?

The thing to understand is that these icons are not used like any image that you can put using an HTML <code>img</code> tag.
The icons are packed together in a small *png* file and are parsed using a special *css* file. This is called a [CSS sprite].
The advantage is that the browser only asks for a single *png* file and a single *css* file for all icons, reducing requests to the server.
But these *png* and *css* were pre-packed in *Twitter Bootstrap* - I simply downloaded *Twitter Bootstrap* and put it in my *static* directory, and from then on I could use icons like this:
<code>
&lt;i class="icon-camera">&lt;/i>
</code>
produces this icon - 
<i class="icon-camera"></i>. 

So how do I use the *Glyphicons Free* icon set, that has 400 icons including my desired <i class="glyphicon-rss"></i>?

At first I downloaded the *Glyphicons Free* set from their website. But this download has two problems:

  - There is no CSS sprite - instead of one *png* and one *css* I got 400 *png*s...
  - The icons are 24x24 pixels, instead of 14x14, like the Halflings...
  
A quick goole led me to a few sites that offered CSS sprites for *Glyphicons Free* (for example [here], 
but each had its own problem. Until I found the right place [rnitkin]. 

### The solution

On this blog post there are both a [glyphicons.png](/static/glyphicons.png) and a [glyphicons.css](/static/glyphicons.css). You can download them and use them.
All you need to do, after putting them on some folder of your site:

  - Add the *css* file to the <code>head</code> of any *HTML* file that uses the icons - change the <code>href</code> accordingly:

<pre class="prettyprint">
&lt;link href="/static/glyphicons.css" rel="stylesheet">
</pre>
  
  - Change the URL of the *png* file in the *css* file to point at where the *png* file is:

<pre class="prettyprint">
background-image: url("images/glyphicons-2.png");
</pre>

  - Alternatively, you can change the URL in the <code>head</code> of your *HTML* file:
  
<pre class="prettyprint">
[class^="glyphicon-"] { background-image: url("/static/glyphicons.png"); } 
</pre>

  - Now you can use icons from *Glyphicons Free* like this:
  
<pre class="prettyprint">
Hospital &lt;i class="glyphicon-hospital"></i>
</pre>
<pre>
Hospital <i class="glyphicon-hospital"></i>
</pre>

  - For a mapping between icon and its name, like the one for *Glyphicons Halflings* on the [Twitter Bootstrap icons documentation], 
  you can check out [MaximaAL's site].

  - Make sure you give proper attribution: the [Glyphicons License] page states that the use of Glyphonics Free is, well, free, 
  but you must include a link to <http://glyphonics.com/> and include the [CC-BY 3.0] license.

### Font Awesome

One last thing. During the search for the solution (15 mins?) I found someone that suggested to use the [Font Awesome] icon set instead of *Glyphicons*, so I tried that.
First of all, the *Font Awesome* site is... awesome. It took me one minute to understand how I need to do, to follow the instructions, and transition my site to *Font Awesome*.
The integration with *Twitter Bootstrap* is very easy. The icon set is large, and it looks nice, but... not as nice as *Glyphonics* looks. So I decided I'd stick with *Glyphicons*.

You can, of course, decide for yourself. Here are screenshots of the navigation bar with [Glyphonics](http://i.imgur.com/3RFfm.png) and here it is with [Font Awesome](http://i.imgur.com/WLVAM.png).
If you would like to see the code, here are the commits for [Glyphonics](https://bitbucket.org/yoavram/msb/changeset/48d36660697bc022548e5476e40157c894aa3a99) and for [Font Awesome](https://bitbucket.org/yoavram/msb/changeset/9a7b530667faeda8da08d9ba932e11622d07287b).

[Glyphicons]: http://glyphicons.com/
[Twitter Bootstrap]: http://twitter.github.com/bootstrap/index.html
[Twitter Bootstrap icons documentation]: http://twitter.github.com/bootstrap/base-css.html#icons
[CC-BY 3.0]: http://creativecommons.org/licenses/by/3.0/
[Glyphicons License]: http://glyphicons.com/glyphicons-licenses/
[web feed]: http://en.wikipedia.org/wiki/Web_feed
[CSS sprite]: http://en.wikipedia.org/wiki/Sprite_(computer_graphics)#Sprites_by_CSS
[MaximaAL's site]: http://maximals.ru/project/sprite/glyphicons/
[here]: http://supercerebral.com/glyphicons-to-halflings-sprite/
[rnitkin]: http://rnikitin.tumblr.com/post/28834314453/all-glyphicons-as-12px-is-css-sprite-fot-bootstrap
[Font Awesome]: http://fortawesome.github.com/Font-Awesome/