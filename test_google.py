import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.google_page import GooglePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome (
        service = Service (ChromeDriverManager().install())
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_google_title(driver):
    page = GooglePage (driver)
    page.open()
    # driver.get("https://www.google.com")
    assert "Google" in driver.title


def test_searchGoogle(driver):
    # driver.get("https://www.google.com")
    page = GooglePage (driver)
    page .open()
    page.search("QA Automation")
    # input = driver.find_element(By.NAME,"q")
    # input.send_keys("QA Automation")
    # input.submit()
    assert "search" in driver.current_url
    