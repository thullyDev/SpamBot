from selenium.webdriver.common.by import By
from ..config import MANGANATO_BASE as BASE, SPAM_COMMENT
from ..caching.cache import Cache
from ..scrapers.natokakalot.natokakalot_scraper import NatoKakalotScraper

cache = Cache()

class NatoKakalot(NatoKakalotScraper):
	def page(self, driver):
		url = self.build_url(base=BASE, endpoint=f"/genre-all/1", params={ "type": "topview" })
		driver.get(url)
		self.comment(driver)
		
	def chapters(self, driver, cached=False):
		url = self.build_url(base=BASE)
		driver.get(url)
		self.comment(driver)

	def mangas(self, driver, page=1, pages=1672, cached=False):
		last_index = 1
		if cached:
			page = cache.get("nato_page")
			last_index = cache.get("nato_last_manga_index")

		for i in range(page, pages + 1):
			mangas = self.get_manga_urls(base=BASE, endpoint=f"genre-all/{page}", params={ "type": "topview" })
			cache.set("nato_page", i)
			
			for index in range(last_index, len(mangas)):
				url = mangas[index]
				driver.get(url)
				# self.comment(driver)
				cache.set("nato_last_manga_index", index)

			

	def comment(self, driver):
		time.sleep(10)
		parent_element = driver.find_element(By.CSS_SELECTOR, ".fb-comments")
		iframe = parent_element.find_element((By.CSS_SELECTOR, "iframe"))
		driver.switch_to.frame(iframe)
		comment_input = driver.find_element(By.CSS_SELECTOR, ".UFIInputContainer .notranslate")
		comment_input.send_keys(SPAM_COMMENT)
		post_btn = driver.find_element(By.CSS_SELECTOR, ".UFIImageBlockContent button.rfloat")
		post_btn.click()
		time.sleep(5)