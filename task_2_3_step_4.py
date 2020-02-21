import time
from helpful_functions import connect_website, quit_connection, find_element, print_code, solve_the_task, accept_allert

browser = connect_website("http://suninjuly.github.io/alert_accept.html")
try:
    find_element(browser, '.btn-primary').click()

    time.sleep(1)

    accept_allert(browser)

    time.sleep(1)

    solve_the_task(browser, '#input_value', '#answer', '.btn-primary')

    print_code(browser)

finally:
    quit_connection(browser)
