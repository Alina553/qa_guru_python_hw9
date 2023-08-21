from selene import browser, by
from selene.support.conditions import be
from selenium import webdriver
from selene.support.shared.jquery_style import s

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
)

# __________________________________________________________________________
#
# Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
#
# ___________________________________________________________________________

def test_without_steps():
    browser.open('https://github.com/')
    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

