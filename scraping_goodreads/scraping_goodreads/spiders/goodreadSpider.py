import data
import sys
start_urls = "http://www.goodreads.com/quotes"
if (data.exists(start_urls)):
    sys.exit(data.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from scraping_goodreads.items import ScrapingGoodreadsItem
    start_urls = "http://www.goodreads.com/quotes"
    class ScrapingGoodreadsSpider(Spider): 
        name = "goodreads"
        allowed_domains = ["www.goodreads.com"]
        start_urls = "http://www.goodreads.com/quotes"
    
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div')
            items = []
            for site in sites:
                item = {}
                item['body'] = str("".join(site.xpath('div[@class="quoteText"]/text()').extract()).encode('UTF-8'))
                item['author'] = str("".join(site.xpath('div[@class="quoteText"]/a/text()').extract()).encode('UTF-8'))
                item['work'] = str("".join(site.xpath('div[@class="quoteText"]/i/a/text()').extract()).encode('UTF-8'))
                if len(item['body']) != 0: 
                    items.append(item)
            data.saveQuotes(self.start_urls,self.allowed_domains,items)
            return 0