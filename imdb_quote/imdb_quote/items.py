# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ImdbQuoteItem(Item):
    # define the fields for your item here like:
    # name = Field()
    quote = Field()
    quote_by = Field()
    pass
