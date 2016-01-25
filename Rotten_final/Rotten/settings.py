# Scrapy settings for Rotten project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Rotten'

SPIDER_MODULES = ['Rotten.spiders']
NEWSPIDER_MODULE = 'Rotten.spiders'
DEFAULT_ITEM_CLASS = 'Rotten.items.RottenItem'
USER_AGENT = '%s' % (BOT_NAME)
ITEMS_PIPELINES = ['Rotten.pipelines.RottenPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Rotten (+http://www.yourdomain.com)'
