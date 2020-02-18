from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from culc_function import solve_the_task, print_code


browser = webdriver.Chrome()
browser.implicitly_wait(1)
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    button=browser.find_element(By.CSS_SELECTOR, '#book')
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button.click()

    solve_the_task(browser, '#input_value', '#answer', "[type=submit]")
    print_code(browser)

finally:
   browser.quit()
