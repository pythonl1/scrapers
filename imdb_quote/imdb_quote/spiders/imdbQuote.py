import dataQuote
import sys

start_urls = "http://www.imdb.com/title/tt1285016/quotes?ref_=tt_ql_3"

if (dataQuote.exists(start_urls)):
    sys.exit(dataQuote.exists(start_urls))  
else:
    from scrapy.spider import BaseSpider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from imdb_quote.items import ImdbQuoteItem

    class ScrapingimdbQuote(BaseSpider): 
        name = "imdb_quote"
        allowed_domains = ["www.imdb.com"]
        start_urls = [
            "http://www.imdb.com/title/tt1285016/quotes?ref_=tt_ql_3",       
        ]
    
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div[@class="quote soda odd"]/p')
            items = []
            for site in sites:
                item = {}
                item['quote'] = str("".join(site.xpath('text()').extract()).encode('UTF-8'))
                item['quote_by'] = str("".join(site.xpath('a/span[@class="character"]/text()').extract()).encode('UTF-8'))
                items.append(item)
            dataQuote.saveQuotes(self.start_urls, self.allowed_domains, items)
            return 0