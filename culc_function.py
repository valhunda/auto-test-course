import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def solve_the_task(browser, input_selector, answer_selector, submit_selector):
    x_element = browser.find_element(By.CSS_SELECTOR, input_selector)
    x = x_element.text
    # print(x)
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, answer_selector)
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, submit_selector)
    button.click()


def print_code(browser):
    alert = browser.switch_to.alert
    alert_text = alert.text

    print(alert_text.split(': ')[-1])
