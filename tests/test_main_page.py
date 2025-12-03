import allure

from pages.main_page import MainPage
from curl import Url


class TestMainPage:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_button_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.wait_until_overlay_disappears()
        main_page.click_on_order_feed()
        main_page.click_button_constructor()
        current_url = main_page.get_current_url()

        assert (
            current_url == Url.main_site
        ), f"Переход не произошел, текущий url - {current_url}"

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.wait_until_overlay_disappears()
        main_page.click_on_order_feed()
        current_url = main_page.get_current_url()

        assert (
            current_url == Url.order_feed
        ), f"Переход не произошел, текущий url - {current_url}"

    @allure.title(
        "Проверка появления всплывающего окна с деталями при клике на ингредиент"
    )
    def test_window_details_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.wait_until_overlay_disappears()
        main_page.click_on_ingredient()

        assert (
            main_page.is_ingredient_details_window_displayed
        ), "Окно с деталями заказа не появилось"

    @allure.title("Проверка закрытия всплывающего окна кликом по крестику")
    def test_close_window_details(self, driver):
        main_page = MainPage(driver)
        main_page.wait_until_overlay_disappears()
        main_page.click_on_ingredient()
        main_page.close_window_details_ingredient()
        main_page.wait_for_window_details_hide()

        assert True, "Окно не закрылось"

    @allure.title(
        "При добавлении ингредиента в заказ счетчик этого ингредиента увеличивается"
    )
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.wait_until_overlay_disappears()
        original_value_counter = main_page.get_ingredient_counter_value()
        main_page.put_ingredient_into_basket()
        value_after_adding = main_page.get_ingredient_counter_value()

        assert (
            original_value_counter < value_after_adding
        ), "Значение счетчика не увеличилось"
