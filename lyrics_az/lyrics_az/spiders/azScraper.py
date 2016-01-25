import data
import sys

start_urls = "http://www.azlyrics.com/lyrics/shakira/empire.html"

if (data.exists(start_urls)):
    sys.exit(data.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from lyrics_az.items import LyricsAzItem
    class LyricsSpiderClass(Spider): 
        name = "lyrics"
        allowed_domains = ["www.azlyrics.com"]
        start_urls = [
            "http://www.azlyrics.com/lyrics/shakira/empire.html",
       
        ]
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div[@id="main"]')
            items = []
            for site in sites:
                item = {}
                item['lyrics'] = "".join(site.xpath('div/text()').extract())
                item['Artist'] = "".join(site.xpath('h2/text()').extract())
                item['Song_name'] = "".join(site.xpath('b/text()').extract())
                if (len(item['lyrics']) != 0): 
                    items.append(item)
            data.saveLyrics(self.start_urls, self.allowed_domains, items)
            return 0