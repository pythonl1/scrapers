from pymongo import MongoClient
import time
Client = MongoClient()
db = Client.scraped_data
def saveReview(start_urls,allowed_domains,items):
	doc={'url':start_urls,
	'domain':allowed_domains,
	'timestamp':time.time(),
	'query':'shawshank redemption',
	'reviews':items,
	}
	db.review_collection.insert(doc)
def exists(start_urls):
	if db.review_collection.find_one({ 'url': start_urls }) != None:
		return db.review_collection.find_one({ 'url': start_urls })
	else :
		return 0