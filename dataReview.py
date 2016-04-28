from pymongo import MongoClient
import time
def saveReviews(start_urls,allowed_domains,items):
	Client = MongoClient()
	db = Client.scraped_data
	doc={'url':start_urls,
	'domain':allowed_domains,
	'timestamp':time.time(),
	'query':'The Dark Knight Rises',
	'reviews':items,
	}
	db.search_collection.insert(doc)
