from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from culc_function import solve_the_task, print_code

# from selenium.webdriver.chrome.service import Service
# import os

browser = webdriver.Opera()
browser.implicitly_wait(1)
link = "http://suninjuly.github.io/explicit_wait2.html"

# использование сервиса для экономии времени

# current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')
# service=Service(r"C:\Users\zalman\PycharmProjects\test_automation\venv\Scripts")
# print(service.service_url)
# service.start()
# browser=webdriver.Remote(service.service_url)


try:
    browser.get(link)
    button=browser.find_element(By.CSS_SELECTOR, '#book')
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button.click()

    solve_the_task(browser)
    print_code(browser)

finally:
   browser.quit()