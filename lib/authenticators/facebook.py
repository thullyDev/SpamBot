from selenium.webdriver.common.by import By
from ..config import (
	FACEBOOK_EMAIL as EMAIL, 
	FACEBOOK_PASSWORD as PASSWORD, 
	FACEBOOK_BASE as BASE
)

class FacebookAuthenticator:
	def __init__(self, driver):
		self.driver = driver
	
	def login(email=EMAIL, password=PASSWORD):
		self.driver.get(f"{BASE}/login.php")
		email_input = self.driver.find_element(By.CSS_SELECTOR, ".inputtext._55r1._1kbt._1kbt") 
		password_input = self.driver.find_element(By.CSS_SELECTOR, ".inputtext._55r1._9npi._9npi")
		login_btn = self.driver.find_element(By.CSS_SELECTOR, "._42ft._4jy0._52e0._4jy6._4jy1._51sy")
		email_input.send_keys(EMAIL)
		password_input.send_keys(PASSWORD)
		login_btn.click()
		time.sleep(10)
