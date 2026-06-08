import logging
from app import LIMIT_KEYWORDS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def find_chatgpt_tab(driver):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)

        if "chatgpt.com" in driver.current_url.lower():
            logging.info(
                f"Tab ditemukan: {driver.current_url}"
            )
            return driver

    return None

def is_limit_reached(driver):

    try:

        page_text = (
            driver.find_element(
                By.TAG_NAME,
                "body"
            )
            .text
            .lower()[:1000]
        )

        print(f"page text adalah {page_text}")

        return any(
            keyword in page_text
            for keyword in LIMIT_KEYWORDS
        )

    except Exception as e:

        logging.error(
            f"Check limit gagal: {e}"
        )

        return False

options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(
    options=options
)

driver = find_chatgpt_tab(driver)

is_limit_reached = is_limit_reached(driver)

if is_limit_reached:
    print("Limit reached")
else:
    print("Limit not reached")