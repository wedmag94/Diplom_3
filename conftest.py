import pytest
from selenium import webdriver
from curl import Url
from pages.main_page import MainPage
from data import Data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Url.main_site)
    yield driver
    driver.quit()


@pytest.fixture  # Фикстура для авторизации пользователя
def login_user(driver):
    main_page = MainPage(driver)
    main_page.wait_until_overlay_disappears()
    main_page.login_button_click()
    main_page.set_field_email(Data.email)
    main_page.set_field_password(Data.password)
    main_page.click_button_enter()
    main_page.wait_until_overlay_disappears()
    return driver
