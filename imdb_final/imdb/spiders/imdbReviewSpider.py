import dataReview
import sys
start_urls = "http://www.imdb.com/title/tt1345836/reviews?ref_=tt_urv"
if (dataReview.exists(start_urls)):
    sys.exit(dataReview.exists(start_urls))  
else:
    from scrapy.spider import BaseSpider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from imdb.items import ImdbItem

    class Scrapingimdb(BaseSpider): 
        name = "imdb_review"
        allowed_domains = ["www.imdb.com"]
        start_urls = [
            "http://www.imdb.com/title/tt1345836/reviews?ref_=tt_urv",       
        ]   
    
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div[@id="tn15content"]/p')
            items = []
            for site in sites:
                item = {}
                item['reviews'] = site.xpath('text()').extract()
                if len(item['reviews']) != 0: 
                    items.append(item)
            dataReview.saveReview(self.start_urls, self.allowed_domains, items)
            return 0