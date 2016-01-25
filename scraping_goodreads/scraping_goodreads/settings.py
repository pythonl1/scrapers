# Scrapy settings for scraping_goodreads project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scraping_goodreads'

SPIDER_MODULES = ['scraping_goodreads.spiders']
NEWSPIDER_MODULE = 'scraping_goodreads.spiders'
DEFAULT_ITEM_CLASS = 'scraping_goodreads.items.ScrapingGoodreadsItem'
USER_AGENT = '%s' % (BOT_NAME)


