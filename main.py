from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from lib import( 
    Cache, 
    FacebookAuthenticator,
    NatoKakalot
)
import typer


app = typer.Typer()
natospam = NatoKakalot()

@app.command()
def nato(driver: str, mode: str, cached: bool=False):
    if driver not in { "chrome", "firefox" }:
        print(f"No such driver as {driver}")
        return

    if mode not in { "page", "mangas" }:
        print(f"No such mode as {mode}")
        return


    driver = chrome_driver() if driver == "chrome" else firefox_driver()
    fb_auth = FacebookAuthenticator()
    fb_auth.login(driver)

    if mode == "mangas": natospam.mangas(driver, cached=cached)
    if mode == "page": natospam.page(driver)


def chrome_driver():
    service = Service(executable_path="chromedriver.exe")
    return webdriver.Chrome(service=service)
    
def firefox_driver():
    return webdriver.Firefox()


if __name__ == "__main__":
    app()
