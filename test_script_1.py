import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

try:
    url = "https://sbis.ru/"
    browser = webdriver.Chrome()
    browser.get(url)

    # Перейти в раздел "Контакты"
    contacts = browser.find_element(By.CSS_SELECTOR, "a[href='/contacts']")
    contacts.click()

    # Найти баннер Тензор, кликнуть по нему
    tenzor_banner = browser.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor img")
    tenzor_banner.click()

    time.sleep(10)

    # human_block = browser.find_element(By.XPATH, '//p[text() = "Сила в людях"]')
    # browser.execute_script("arguments[0].scrollIntoView(true);", human_block)
    human_block = browser.find_element(By.CSS_SELECTOR, 'a.tensor_ru-link[href="/about"]')
    human_block.location_once_scrolled_into_view
    human_block.click()

    # human_block_more = browser.find_element(By.CSS_SELECTOR, "//a[contains(@class, 'tensor_ru-link tensor_ru-Index__link') and @href='/about']")
    # human_block_more.click()

finally:
    time.sleep(5)
    browser.quit()