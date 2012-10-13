/*
*  How to use the Dynamic Feed Control, which has pretty UI already made for you!
*  Don't forget to check out the options:
*  http://www.google.com/uds/solutions/dynamicfeed/reference.html
*/

google.load('feeds', '1');

function OnLoad() {
  var feeds = [
   /* {
      title: 'Bitbucket',
      url: 'https://bitbucket.org/yoavram/rss/feed?token=a18fd7c2b7e99a48083800d00fccce2f'
    },*/
	{
		title: 'Recent Posts',
		url: 'http://yoavram.bitbucket.org/recent.atom'
	},
	 {
      title: 'Publications',
      url: 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/erss.cgi?rss_guid=1RukBFKPvabUOwpqbC3ttHi8F4FuasZqQqkc1ePwc-qWGdC1Y8'
    }
  ];

  var options = {
    stacked : true,
    horizontal : false,
    title : "Feeds"
  };

  new GFdynamicFeedControl(feeds, 'feed-content', options);
  document.getElementById('feed-content').style.width = "200px";
}

google.setOnLoadCallback(OnLoad);