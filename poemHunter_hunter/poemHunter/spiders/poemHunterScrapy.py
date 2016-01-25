import dataPoem
import sys
start_urls = "http://www.poemhunter.com/poem/nature-is-what-we-see/"
if (dataPoem.exists(start_urls)):
    sys.exit(dataPoem.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from poemHunter.items import PoemhunterItem
    class Scrapingpoem(Spider): 
        name = "poemHunter"
        allowed_domains = ["www.poemhunter.com"]
        start_urls = [
            "http://www.poemhunter.com/poem/nature-is-what-we-see/",       
        ]
    
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div')
            items = []
            item_title = []
            item_poem = []
            item_poet = []
            final_item = []
            for site in sites:
                item = {}
                item['title'] = "".join(site.xpath('h2[@itemprop="name"]/text()').extract())
                item['poem'] = "".join(site.xpath('div[@class="KonaBody"]/p/text()').extract())
                item['poet'] = site.xpath('div[@itemprop="author"]/text()').extract()
                if (len(item['poet']) != 0):
                    item_poet.append(item['poet'])
                if (len(item['poem']) != 0):
                    item_poem.append(item['poem'])
                if (len(item['title']) != 0):
                    item_title.append(item['title'])
            final = {}
            final['poet'] = item_poet
            final['poem'] = item_poem
            final['title'] = item_title
            final_item.append(final)
            dataPoem.savePoems(self.start_urls, self.allowed_domains, final_item)
            return 0
            
                 

