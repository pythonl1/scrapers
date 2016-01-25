class TestPipeline(object):
    def process_item(self, item, spider_new):
            print item['reviews']