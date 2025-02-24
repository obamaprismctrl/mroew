dorking_methods = [
        {"name": "Facebook", "link": '"{username}" site:facebook.com'},
        {"name": "Twitter", "link": '"{username}" site:twitter.com'},
        {"name": "LinkedIn", "link": '"{username}" site:linkedin.com'},
        {"name": "GitHub", "link": '"{username}" site:github.com'},
        {"name": "Gmail", "link": '"{username}" "@gmail.com"'},
        {"name": "Yahoo", "link": '"{username}" "@yahoo.com"'},
        {"name": "Comments", "link": '"{username}" inurl:comments'},
        {"name": "Text Files", "link": '"{username}" filetype:txt'},
        {"name": "Cache", "link": 'cache:"{username}"'},
        {"name": "Blogspot", "link": '"{username}" site:blogspot.com'},
        {"name": "PDF Files", "link": '"{username}" filetype:pdf'},
        {"name": "Doc Files", "link": '"{username}" filetype:doc'},
        {"name": "Reddit", "link": '"{username}" site:reddit.com'},
        {"name": "Indeed", "link": '"{username}" site:indeed.com'},
        {"name": "Whois Domain Tools", "link": '"{username}" site:whois.domaintools.com'},
        {"name": "Pastebin", "link": '"{username}" site:pastebin.com'},
        {"name": "Yellow Pages", "link": '"{username}" site:yellowpages.com'},
        {"name": "Data.com", "link": '"{username}" site:data.com'},
        {"name": "Profile", "link": '"{username}" inurl:profile'},
        {"name": "Listserv", "link": '"{username}" site:listserv.com'},
        {"name": "GitLab", "link": '"{username}" site:gitlab.com'},
        {"name": "ResearchGate", "link": '"{username}" site:researchgate.net'},
        {"name": "Medium", "link": '"{username}" site:medium.com'},
        {"name": "StackOverflow", "link": '"{username}" site:stackoverflow.com'},
        {"name": "Pinterest", "link": '"{username}" site:pinterest.com'},
        {"name": "Quora", "link": '"{username}" site:quora.com'},
        {"name": "Instagram", "link": '"{username}" site:instagram.com'},
        {"name": "Tumblr", "link": '"{username}" site:tumblr.com'},
        {"name": "Vimeo", "link": '"{username}" site:vimeo.com'},
        {"name": "YouTube", "link": '"{username}" site:youtube.com'},
        {"name": "WordPress", "link": '"{username}" site:wordpress.com'},
        {"name": "Amazon", "link": '"{username}" site:amazon.com'},
        {"name": "Bank", "link": '"{username}" site:bank.com'},
        {"name": "Spokeo", "link": '"{username}" site:spokeo.com'},
        {"name": "PeopleFinder", "link": '"{username}" site:peoplefinder.com'},
        {"name": "Classmates", "link": '"{username}" site:classmates.com'},
        {"name": "MySpace", "link": '"{username}" site:myspace.com'},
        {"name": "Search Yahoo", "link": '"{username}" site:search.yahoo.com'},
        {"name": "Apple", "link": '"{username}" site:apple.com'},
        {"name": "IMDB", "link": '"{username}" site:imdb.com'},
        {"name": "PirateBay", "link": '"{username}" site:thepiratebay.org'},
        {"name": "WikiHow", "link": '"{username}" site:wikihow.com'},
        {"name": "Scribd", "link": '"{username}" site:scribd.com'},
        {"name": "ZipRecruiter", "link": '"{username}" site:ziprecruiter.com'},
        {"name": "Expedia", "link": '"{username}" site:expedia.com'},
        {"name": "LinkedIn Profile", "link": '"{username}" site:linkedin.com/in/'},
        {"name": "Academia", "link": '"{username}" site:academia.edu'},
        {"name": "WhosWho", "link": '"{username}" site:whoswho.com'},
        {"name": "AngelList", "link": '"{username}" site:angel.co'},
        {"name": "Slideshare", "link": '"{username}" site:slideshare.net'},
        {"name": "SpyCloud", "link": '"{username}" site:spycloud.com'},
        {"name": "ICQ", "link": '"{username}" site:icq.com'},
        {"name": "Live.com", "link": '"{username}" site:login.live.com'},
        {"name": "Match.com", "link": '"{username}" site:match.com'},
        {"name": "Wellness", "link": '"{username}" site:wellness.com'},
        {"name": "Behance", "link": '"{username}" site:behance.net'},
        {"name": "Dribbble", "link": '"{username}" site:dribbble.com'},
        {"name": "Genius", "link": '"{username}" site:genius.com'},
        {"name": "Goodreads", "link": '"{username}" site:goodreads.com'},
        {"name": "Badoo", "link": '"{username}" site:badoo.com'},
        {"name": "Skype", "link": '"{username}" site:skype.com'},
        {"name": "Tinder", "link": '"{username}" site:tinder.com'},
        {"name": "OkCupid", "link": '"{username}" site:okcupid.com'},
        {"name": "Plenty of Fish", "link": '"{username}" site:pof.com'},
        {"name": "Hinge", "link": '"{username}" site:hinge.co'},
        {"name": "Zoosk", "link": '"{username}" site:zoosk.com'},
        {"name": "Grindr", "link": '"{username}" site:grindr.com'},
        {"name": "Adam4Adam", "link": '"{username}" site:adam4adam.com'},
        {"name": "AdultFriendFinder", "link": '"{username}" site:adultfriendfinder.com'},
        {"name": "Blued", "link": '"{username}" site:blued.com'},
        {"name": "Her", "link": '"{username}" site:weareher.com'},
        {"name": "Meetup", "link": '"{username}" site:meetup.com'},
        {"name": "Flickr", "link": '"{username}" site:flickr.com'},
        {"name": "DeviantArt", "link": '"{username}" site:deviantart.com'},
        {"name": "SoundCloud", "link": '"{username}" site:soundcloud.com'},
        {"name": "Twitch", "link": '"{username}" site:twitch.tv'},
        {"name": "Discord", "link": '"{username}" site:discord.com'},
        {"name": "Telegram", "link": '"{username}" site:telegram.org'},
        {"name": "WhatsApp", "link": '"{username}" site:whatsapp.com'},
        {"name": "Signal", "link": '"{username}" site:signal.org'},
        {"name": "Snapchat", "link": '"{username}" site:snapchat.com'},
        {"name": "TikTok", "link": '"{username}" site:tiktok.com'},
        {"name": "WeChat", "link": '"{username}" site:wechat.com'},
        {"name": "VKontakte", "link": '"{username}" site:vk.com'},
        {"name": "Xing", "link": '"{username}" site:xing.com'},
        {"name": "Crunchbase", "link": '"{username}" site:crunchbase.com'},
        {"name": "Kickstarter", "link": '"{username}" site:kickstarter.com'},
        {"name": "Indiegogo", "link": '"{username}" site:indiegogo.com'},
        {"name": "Patreon", "link": '"{username}" site:patreon.com'},
        {"name": "Etsy", "link": '"{username}" site:etsy.com'},
        {"name": "eBay", "link": '"{username}" site:ebay.com'},
        {"name": "AliExpress", "link": '"{username}" site:aliexpress.com'},
        {"name": "Walmart", "link": '"{username}" site:walmart.com'},
        {"name": "Target", "link": '"{username}" site:target.com'},
        {"name": "BestBuy", "link": '"{username}" site:bestbuy.com'},
        {"name": "Zillow", "link": '"{username}" site:zillow.com'},
        {"name": "Realtor", "link": '"{username}" site:realtor.com'},
        {"name": "Trulia", "link": '"{username}" site:trulia.com'},
        {"name": "Zoopla", "link": '"{username}" site:zoopla.co.uk'},
        {"name": "Rightmove", "link": '"{username}" site:rightmove.co.uk'},
        {"name": "Booking.com", "link": '"{username}" site:booking.com'},
        {"name": "Airbnb", "link": '"{username}" site:airbnb.com'},
        {"name": "TripAdvisor", "link": '"{username}" site:tripadvisor.com'},
        {"name": "Yelp", "link": '"{username}" site:yelp.com'},
        {"name": "Glassdoor", "link": '"{username}" site:glassdoor.com'},
        {"name": "Monster", "link": '"{username}" site:monster.com'},
        {"name": "CareerBuilder", "link": '"{username}" site:careerbuilder.com'},
        {"name": "SimplyHired", "link": '"{username}" site:simplyhired.com'},
        {"name": "Dice", "link": '"{username}" site:dice.com'},
        {"name": "Upwork", "link": '"{username}" site:upwork.com'},
        {"name": "Freelancer", "link": '"{username}" site:freelancer.com'},
        {"name": "Fiverr", "link": '"{username}" site:fiverr.com'},
        {"name": "Toptal", "link": '"{username}" site:toptal.com'},
        {"name": "99Designs", "link": '"{username}" site:99designs.com'},
        {"name": "ArtStation", "link": '"{username}" site:artstation.com'},
        {"name": "500px", "link": '"{username}" site:500px.com'},
        {"name": "VSCO", "link": '"{username}" site:vsco.co'},
        {"name": "Pexels", "link": '"{username}" site:pexels.com'},
        {"name": "Unsplash", "link": '"{username}" site:unsplash.com'},
        {"name": "Shutterstock", "link": '"{username}" site:shutterstock.com'},
        {"name": "Getty Images", "link": '"{username}" site:gettyimages.com'},
        {"name": "Adobe Stock", "link": '"{username}" site:stock.adobe.com'},
        {"name": "Alamy", "link": '"{username}" site:alamy.com'},
        {"name": "iStock", "link": '"{username}" site:istockphoto.com'},
        {"name": "Depositphotos", "link": '"{username}" site:depositphotos.com'},
        {"name": "Dreamstime", "link": '"{username}" site:dreamstime.com'},
        {"name": "123RF", "link": '"{username}" site:123rf.com'},
        {"name": "Bigstock", "link": '"{username}" site:bigstockphoto.com'},
        {"name": "Canva", "link": '"{username}" site:canva.com'},
        {"name": "Figma", "link": '"{username}" site:figma.com'},
        {"name": "InVision", "link": '"{username}" site:invisionapp.com'},
        {"name": "Sketch", "link": '"{username}" site:sketch.com'},
        {"name": "Marvel", "link": '"{username}" site:marvelapp.com'},
        {"name": "Proto.io", "link": '"{username}" site:proto.io'},
        {"name": "Axure", "link": '"{username}" site:axure.com'},
        {"name": "Balsamiq", "link": '"{username}" site:balsamiq.com'},
        {"name": "Moqups", "link": '"{username}" site:moqups.com'},
        {"name": "Lucidchart", "link": '"{username}" site:lucidchart.com'},
        {"name": "Miro", "link": '"{username}" site:miro.com'},
        {"name": "Whimsical", "link": '"{username}" site:whimsical.com'},
        {"name": "Zeplin", "link": '"{username}" site:zeplin.io'},
        {"name": "Abstract", "link": '"{username}" site:abstract.com'},
        {"name": "Avocode", "link": '"{username}" site:avocode.com'},
        {"name": "Principle", "link": '"{username}" site:principleformac.com'},
        {"name": "Framer", "link": '"{username}" site:framer.com'},
        {"name": "Webflow", "link": '"{username}" site:webflow.com'},
        {"name": "Wix", "link": '"{username}" site:wix.com'},
        {"name": "Squarespace", "link": '"{username}" site:squarespace.com'},
        {"name": "WordPress.org", "link": '"{username}" site:wordpress.org'},
        {"name": "Joomla", "link": '"{username}" site:joomla.org'},
        {"name": "Drupal", "link": '"{username}" site:drupal.org'},
        {"name": "Magento", "link": '"{username}" site:magento.com'},
        {"name": "Shopify", "link": '"{username}" site:shopify.com'},
        {"name": "BigCommerce", "link": '"{username}" site:bigcommerce.com'},
        {"name": "WooCommerce", "link": '"{username}" site:woocommerce.com'},
        {"name": "PrestaShop", "link": '"{username}" site:prestashop.com'},
        {"name": "OpenCart", "link": '"{username}" site:opencart.com'},
        {"name": "osCommerce", "link": '"{username}" site:oscommerce.com'},
        {"name": "Zen Cart", "link": '"{username}" site:zen-cart.com'},
        {"name": "Volusion", "link": '"{username}" site:volusion.com'},
        {"name": "3dcart", "link": '"{username}" site:3dcart.com'},
        {"name": "Weebly", "link": '"{username}" site:weebly.com'},
        {"name": "Jimdo", "link": '"{username}" site:jimdo.com'},
        {"name": "Strikingly", "link": '"{username}" site:strikingly.com'},
        {"name": "Carrd", "link": '"{username}" site:carrd.co'},
        {"name": "Tilda", "link": '"{username}" site:tilda.cc'},
        {"name": "Webnode", "link": '"{username}" site:webnode.com'},
        {"name": "Site123", "link": '"{username}" site:site123.com'},
        {"name": "Ucraft", "link": '"{username}" site:ucraft.com'},
        {"name": "Bookmark", "link": '"{username}" site:bookmark.com'},
        {"name": "Duda", "link": '"{username}" site:duda.co'},
        {"name": "GoDaddy Website Builder", "link": '"{username}" site:godaddy.com'},
        {"name": "IM Creator", "link": '"{username}" site:imcreator.com'},
        {"name": "Mobirise", "link": '"{username}" site:mobirise.com'},
        {"name": "Pixpa", "link": '"{username}" site:pixpa.com'},
        {"name": "SiteBuilder", "link": '"{username}" site:sitebuilder.com'},
        {"name": "Sitejet", "link": '"{username}" site:sitejet.io'},
        {"name": "Zoho Sites", "link": '"{username}" site:zoho.com/sites'},
        {"name": "Zyro", "link": '"{username}" site:zyro.com'},
        {"name": "Google Sites", "link": '"{username}" site:sites.google.com'},
        {"name": "GitHub Pages", "link": '"{username}" site:github.io'},
        {"name": "GitLab Pages", "link": '"{username}" site:gitlab.io'},
        {"name": "Netlify", "link": '"{username}" site:netlify.com'},
        {"name": "Vercel", "link": '"{username}" site:vercel.com'},
        {"name": "Surge", "link": '"{username}" site:surge.sh'},
        {"name": "Render", "link": '"{username}" site:render.com'},
        {"name": "Firebase", "link": '"{username}" site:firebase.com'},
        {"name": "Heroku", "link": '"{username}" site:heroku.com'},
]