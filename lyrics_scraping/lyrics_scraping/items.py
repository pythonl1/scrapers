# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LyricsScrapingItem(Item):
    # define the fields for your item here like:
    # name = Field()
    lyrics = Field()
    Song_name = Field()
    Artist = Field()
    album_name = Field()
    pass
