import data
import sys
start_urls = "http://en.wikiquote.org/wiki/Douglas_Adams"
if (data.exists(start_urls)):
    sys.exit(data.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from scraping_wikiquotes.items import ScrapingWikiquotesItem
    import data

    class ScrapingWikiquotesSpider(Spider): 
        name = "wikiquotes"
        allowed_domains = ["wikiquotes.org"]
        start_urls = "http://en.wikiquote.org/wiki/Douglas_Adams",
    
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//ul')
            items = []
            for site in sites:
                item = {}
                item['quotes'] = site.xpath('li/b/text()').extract()
                if len(item['quotes']) != 0: 
                    items.append(item)
            data.saveQuotes(self.start_urls, self.allowed_domains, items)
            return 0