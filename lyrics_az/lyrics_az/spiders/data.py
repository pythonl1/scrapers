from pymongo import MongoClient
import time
Client = MongoClient()
db = Client.scraped_data
def saveLyrics(start_urls,allowed_domains,items):
	doc={'url':start_urls,
	'domain':allowed_domains,
	'timestamp':time.time(),
	'query':'shawshank redemption',
	'lyrics':items,
	}
	db.lyrics_collection.insert(doc)
def exists(start_urls):
	if db.lyrics_collection.find_one({ 'url': start_urls }) != None:
		return db.lyrics_collection.find_one({ 'url': start_urls })
	else :
		return 0