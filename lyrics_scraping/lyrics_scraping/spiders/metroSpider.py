import dataLyrics
import sys

start_urls = "http://www.metrolyrics.com/in-the-end-lyrics-linkin-park.html"

if (dataLyrics.exists(start_urls)):
    sys.exit(dataLyrics.exists(start_urls))  
else:
    from scrapy.spider import Spider
    from scrapy.selector import Selector
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from lyrics_scraping.items import LyricsScrapingItem

    class LyricsSpiderClass(Spider): 
        name = "metro"
        allowed_domains = ["www.metrolyrics.com"]
        start_urls = [
            "http://www.metrolyrics.com/in-the-end-lyrics-linkin-park.html",
       
        ]
        def parse(self, response):
            sel = Selector(response)
            sites = sel.xpath('//div')
            items = []
            items_art = [] #for filtering the empty items
            items_lyr = [] #for filterring the empty items
            items_sng = [] #for filterring the empty items
            final_items = []
            for site in sites:
                item = {}
                item['Artist'] = site.xpath('div[@class="grid_6 suffix_6"]/h1/text()').extract()
                item['lyrics'] = site.xpath('div[@id="lyrics-body-text"]/p[@class="verse"]/text()').extract()
                item['Song_name'] = site.xpath('header/h1/text()').extract()
                if (len(item['Artist']) != 0):
                    items_art.append(item['Artist'])
                if (len(item['lyrics']) != 0):
                    items_lyr.append(item['lyrics'])
                if (len(item['Song_name']) != 0):
                    items_sng.append(item['Song_name'])
            final = {}
            final['Artist'] = items_art
            final['Song_name'] = items_sng
            final['lyrics'] = items_lyr
            final_items.append(final)
            dataLyrics.saveLyrics(self.start_urls, self.allowed_domains, final_items)
            return 0