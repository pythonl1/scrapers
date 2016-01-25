import dataPoem
import sys
start_urls = "http://www.poetryfoundation.org/poetrymagazine/poem/246346"
if (dataPoem.exists(start_urls)):
    sys.exit(dataPoem.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from poetryFoundation.items import PoetryfoundationItem
    class poem_foundation(Spider): 
        name = "poem"
        allowed_domains = ["http://www.poetryfoundation.org/"]
        start_urls = [
            "http://www.poetryfoundation.org/poetrymagazine/poem/246346",
       
        ]
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div')
            items = []
            item_poet = []
            item_title = []
            item_poem = []
            final_item = []
            for site in sites:
                item = {}
                item['poet'] = site.xpath('div[@id="poemwrapper"]/span[@class="author"]/a/text()').extract()
                item['title'] = site.xpath('div[@id="poem-top"]/h1/text()').extract()
                item['poem'] = site.xpath('div[@class="poem"]/div/text()').extract()
                if (len(item['poet']) != 0):
                    item_poet.append(item['poet'])
                if (len(item['title']) != 0):
                    item_title.append(item['title'])
                if (len(item['poem']) != 0):
                    item_poem.append(item['poem'])
            final = {}
            final['poem'] = item_poem
            final['poet'] = item_poet
            final['title'] = item_title
            final_item.append(final)
            dataPoem.savePoems(self.start_urls, self.allowed_domains, final_item)
            return 0