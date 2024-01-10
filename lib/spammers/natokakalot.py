from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ..config import MANGANATO_BASE as BASE, SPAM_COMMENT
from ..caching.cache import Cache
from ..scrapers.natokakalot.natokakalot_scraper import NatoKakalotScraper
import time

cache = Cache()

class NatoKakalot(NatoKakalotScraper):
    def page(self, driver):
        url = self.build_url(base=BASE, endpoint=f"/genre-all/1", params={ "type": "topview" })
        driver.get(url)
        self.comment(driver)
        
    def mangas(self, driver, page=1, pages=1672, cached=False):
        last_index = 0
        if cached:
            page = cache.get("nato_page", 1)
            last_index = cache.get("nato_last_manga_index", 1)

        for i in range(page, pages + 1):
            mangas = self.get_manga_urls(base=BASE, endpoint=f"genre-all/{i}", params={ "type": "topview" })
            cache.set("nato_page", i)
            
            for index in range(last_index, len(mangas)):
                url = mangas[index]
                driver.get(url)
                self.comment(driver)
                cache.set("nato_last_manga_index", index)

    def comment(self, driver):
        TIME_OUT = 60
        time.sleep(10)
        element_to_scroll_to = driver.find_element(By.CLASS_NAME, "fb-comment-title")
        actions = ActionChains(driver)
        actions.move_to_element(element_to_scroll_to).perform()
        scroll_script = "window.scrollBy(0, 200);"
        driver.execute_script(scroll_script)
        driver.implicitly_wait(10)

        # time.sleep(10)
        parent_element = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.CLASS_NAME, "fb-comments")))
        iframe = WebDriverWait(parent_element, TIME_OUT).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)
        comment_input = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".UFIInputContainer .notranslate")))

        comment_input.send_keys(SPAM_COMMENT)
        post_btn = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".UFIImageBlockContent button.rfloat")))
        post_btn = driver.find_element(By.CSS_SELECTOR, "")
        post_btn.click()
        time.sleep(2)

        driver.switch_to.default_content()

    # def wait_selector(self, driver, type_selector, selector, TIME_OUT):
    # 	if type_selector == "class":


