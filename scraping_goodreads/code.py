import web
from scraping_goodreads.spiders.goodread_spider import scraper

urls = (
    '/', 'index', '/search','search'
)

class index:
    def GET(self):
        return "Hello, world!"
class search:
    def GET(self):
        return scraper()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
