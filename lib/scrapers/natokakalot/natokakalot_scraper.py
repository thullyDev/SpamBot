from ...handlers.scraper import Scraper
from .blueprints import mangas_blueprint, chapters_blueprint
from pprint import pprint as printt

# self.driver.get("https://manganato.com/genre-all/8?type=topview")

class NatoKakalotScraper(Scraper):
	def get_chapters(self, url):
		pass

	def get_manga_urls(self, base, endpoint="", params={}):
		rawdata = self.get(base=base, endpoint=endpoint, params=params, blueprint=mangas_blueprint)
		data = []

		for item in rawdata["mangas"]:
			url = item["manga_slug"]["slug"]
			data.append(url)

		return data
