import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def connect_website(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)
    return browser


def quit_connection(browser):
    browser.quit()


def find_element(browser, selector):
    return browser.find_element(By.CSS_SELECTOR, selector)


def set_value_for_field(field, value):
    field.send_keys(value)


def find_element_by_tag(browser, tag):
    return browser.find_element(By.TAG_NAME, tag)


def checking_registration(link):
    browser = connect_website(link)
    set_value_for_field(find_element(browser, '.first_block .first'), "Ivan")
    set_value_for_field(find_element(browser, '.first_block .second'), "Petrov")
    set_value_for_field(find_element(browser, '.third'), "aab@rambler.ru")
    find_element(browser, 'button.btn').click()
    welcome_text = find_element_by_tag(browser, 'h1').text
    quit_connection(browser)
    return welcome_text


def accept_allert(browser):
    confirm = browser.switch_to.alert
    confirm.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def solve_the_task(browser, input_selector, answer_selector, submit_selector):
    answer = calc(find_element(browser, input_selector).text)
    # print(answer)
    set_value_for_field(find_element(browser, answer_selector), answer)
    find_element(browser, submit_selector).click()


def print_code(browser):
    alert = browser.switch_to.alert
    alert_text = alert.text

    print(alert_text.split(': ')[-1])
