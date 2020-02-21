from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpful_functions import connect_website, quit_connection, find_element, solve_the_task, print_code

browser = connect_website("http://suninjuly.github.io/explicit_wait2.html")
try:
    button = find_element(browser, '#book')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    solve_the_task(browser, '#input_value', '#answer', "[type=submit]")
    print_code(browser)

finally:
    quit_connection(browser)
