import dataReview
import sys

start_urls = "http://www.rottentomatoes.com/m/iron_man/"

if (dataReview.exists(start_urls)):
    sys.exit(dataReview.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from Rotten.items import RottenItem
    
    class Scrapingrotten(Spider): 
        name = "rottentomatoes"
        allowed_domains = ["www.rottentomatoes.com"]
        start_urls = "http://www.rottentomatoes.com/m/iron_man/",
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div')
            items = []
            items_rv = [] #for filtering the empty items
            items_cr = [] #for filterring the empty items
            final_items = []
            for site in sites:
                item = {}
                item['reviews'] = site.xpath('div[@class="media_block_content"]/p/text()').extract()
                item['critic'] = site.xpath('div[@class="bold"]/a/text()').extract()
                if (len(item['reviews'])!=0):
                    items_rv.append(item['reviews'])
                if(len(item['critic'])!=0):
                    items_cr.append(item['critic'])
                for x in range(len(items_cr)-1):
                    final  = {}
                    final['reviews'] = items_rv[x]
                    final['critic'] = items_cr[x]
                final_items.append(final)
            dataReview.saveReviews(self.start_urls, self.allowed_domains, final_items)
            return 0
