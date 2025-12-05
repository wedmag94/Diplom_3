import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import Url


class MainPage(BasePage):
    @allure.step("Ждем невидимости оверлея")
    def wait_until_overlay_disappears(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Кликнуть на кнопку Конструктор")
    def click_button_constructor(self):
        self.wait_element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BOTTON)
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BOTTON)

    @allure.step("Кликнуть на кнопку Лента заказов")
    def click_on_order_feed(self):
        # self.wait_element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_on_ingredient(self):
        self.wait_element_to_be_clickable(MainPageLocators.INGREDIENT)
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step("Дождаться отображения окна с деталями ингредиента")
    def is_ingredient_details_window_displayed(self):
        return self.find_element_with_wait(
            MainPageLocators.WINDOW_DETAILS_INGREDIENT
        ).is_displayed()

    @allure.step("Закрыть всплывающее окно")
    def close_window_details_ingredient(self):
        self.wait_element_to_be_clickable(MainPageLocators.WINDOW_DETAILS_INGREDIENT)
        self.click_to_element(MainPageLocators.CLOSING_WINDOW)

    @allure.step("Дождаться пока окно с деталями ингредиента станет невидимым")
    def wait_for_window_details_hide(self):
        return self.wait_for_element_hide(MainPageLocators.WINDOW_DETAILS_INGREDIENT)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        self.wait_for_element(MainPageLocators.COUNTER_INGREDIENT)
        return self.find_element_with_wait(MainPageLocators.COUNTER_INGREDIENT).text

    @allure.step("Перетащить элемент в корзину")
    def put_ingredient_into_basket(self):
        self.wait_until_overlay_disappears()
        ingredient = self.find_element_with_wait(locator=MainPageLocators.INGREDIENT)
        basket = self.find_element_with_wait(locator=MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Нажать кнопку Войти в аккаунт")
    def login_button_click(self):
        self.wait_element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        self.click_to_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Заполнить поле Email")
    def set_field_email(self, email):
        self.send_keys_to_input(MainPageLocators.INPUT_EMAIL, email)

    @allure.step("Заполнить поле Пароль")
    def set_field_password(self, password):
        self.send_keys_to_input(MainPageLocators.INPUT_PASSWORD, password)

    @allure.step("Нажать кнопку Войти")
    def click_button_enter(self):
        self.wait_element_to_be_clickable(MainPageLocators.BUTTON_ENTER)
        self.click_to_element(MainPageLocators.BUTTON_ENTER)

    @allure.step("Кликнуть на кнопку Оформить заказ")
    def click_to_button_place_order(self):
        self.wait_element_to_be_clickable(MainPageLocators.BUTTON_PLACE_ORDER)
        self.click_to_element(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("Открыть Ленту заказов")
    def open_order_feed_page(self):
        self.open_page(Url.order_feed)
