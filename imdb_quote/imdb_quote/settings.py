# Scrapy settings for imdb_quote project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imdb_quote'

SPIDER_MODULES = ['imdb_quote.spiders']
NEWSPIDER_MODULE = 'imdb_quote.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imdb_quote (+http://www.yourdomain.com)'
