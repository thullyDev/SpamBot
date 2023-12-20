from selenium.webdriver.common.by import By
from ..config import (
	FACEBOOK_EMAIL as EMAIL, 
	FACEBOOK_PASSWORD as PASSWORD, 
	FACEBOOK_BASE as BASE
)
import time

class FacebookAuthenticator:
	def login(self, driver):
		driver.get(f"{BASE}/login.php")
		email_input = driver.find_element(By.CSS_SELECTOR, ".inputtext._55r1._1kbt._1kbt") 
		password_input = driver.find_element(By.CSS_SELECTOR, ".inputtext._55r1._9npi._9npi")
		login_btn = driver.find_element(By.CSS_SELECTOR, "._42ft._4jy0._52e0._4jy6._4jy1._51sy")
		email_input.send_keys(EMAIL)
		password_input.send_keys(PASSWORD)
		login_btn.click()
		time.sleep(10)
