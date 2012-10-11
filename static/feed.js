/*
*  How to load a feed via the Feeds API.
*  http://code.google.com/apis/ajax/playground/#load_feed
*/

google.load("feeds", "1");

// Our callback function, for when a feed is loaded.
function feedLoaded(result, target) {
  if (!result.error) {
    // Grab the container we will put the results into
    var container = document.getElementById(target);
	container.class = "publication-list";
    container.innerHTML = '';

    // Loop through the feeds, putting the titles onto the page.
    // Check out the result object for a list of properties returned in each entry.
    // http://code.google.com/apis/ajaxfeeds/documentation/reference.html#JSON
	var ul = document.createElement("ul");
	ul.className = "unstyled";
    for (var i = 0; i < result.feed.entries.length; i++) {
      var entry = result.feed.entries[i];
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.title = entry.title;
      a.innerHTML = '<i class="icon-ok"></i> '+a.title;
      a.href = entry.link;
      li.appendChild(a);
      ul.appendChild(li);
    }
	container.appendChild(ul);
  }
}

function OnLoad() {
  // Create a feed instance that will grab the publication list from PubMed
  // http://rtfmed.wordpress.com/2011/11/11/creating-cusomized-rss-alerts-for-scientific-articles/
  var pubmed_feed = new google.feeds.Feed("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/erss.cgi?rss_guid=1RukBFKPvabUOwpqbC3ttHi8F4FuasZqQqkc1ePwc-qWGdC1Y8");
  var bitbucket_feed = new google.feeds.Feed("https://bitbucket.org/yoavram/rss/feed?token=a18fd7c2b7e99a48083800d00fccce2f");

  // Calling load sends the request off.  It requires a callback function.
  pubmed_feed.load(feedLoaded, "pubmed-content");
  bitbucket_feed.load(feedLoaded, "bitbucket-content");

}

google.setOnLoadCallback(OnLoad);