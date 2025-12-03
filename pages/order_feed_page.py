import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Получить номер заказа, присвоенный при оформлении")
    def get_number_order(self):
        self.wait_for_element(OrderFeedPageLocators.NUMBER_ORDER)
        return self.find_element_with_wait(OrderFeedPageLocators.NUMBER_ORDER).text

    @allure.step("Закрыть окно с номером заказа")
    def close_window_number_order(self):
        self.wait_element_to_be_clickable(
            OrderFeedPageLocators.BUTTON_CLOSE_ORDER_NUMBER
        )
        self.click_to_element(OrderFeedPageLocators.BUTTON_CLOSE_ORDER_NUMBER)

    @allure.step("Получить значение счетчика Выполнено за все время")
    def get_order_counter_for_entire_time(self):
        self.wait_for_element(OrderFeedPageLocators.ORDER_COUNTER_FOR_ENTIRE_TIME)
        return self.find_element_with_wait(
            OrderFeedPageLocators.ORDER_COUNTER_FOR_ENTIRE_TIME
        ).text

    @allure.step("Получить значение счетчика Выполнено за сегодня")
    def get_order_counter_for_day(self):
        self.scroll_to_element(OrderFeedPageLocators.COUNTER_ORDER_FOR_DAY)
        return self.find_element_with_wait(
            OrderFeedPageLocators.COUNTER_ORDER_FOR_DAY
        ).text

    @allure.step("Получить номер заказа В работе")
    def get_number_order_in_progress(self):
        self.wait_for_element(OrderFeedPageLocators.NUMBER_ORDER_IN_PROGRESS)
        return self.find_element_with_wait(
            OrderFeedPageLocators.NUMBER_ORDER_IN_PROGRESS
        ).text
