import pytest
import time
from selenium.webdriver.common.by import By

def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, f"Button not found"

if __name__ == "__main__":
    pytest.main()