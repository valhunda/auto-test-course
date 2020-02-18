from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from culc_function import calc, print_code, solve_the_task

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button_first = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button_first.click()

    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    solve_the_task(browser, '#input_value', '#answer', '.btn-primary')

    print_code(browser)

finally:
    # time.sleep(3)
    browser.quit()
