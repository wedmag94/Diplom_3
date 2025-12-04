import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title("При создании заказа счетчик 'Выполнено за все время' увеличивается")
    def test_order_counter_for_entire_time(self, login_user):
        main_page = MainPage(login_user)
        order_feed_page = OrderFeedPage(login_user)
        main_page.click_on_order_feed()
        initial_counter_value = order_feed_page.get_order_counter_for_entire_time()
        main_page.click_button_constructor()
        main_page.wait_until_overlay_disappears()
        main_page.put_ingredient_into_basket()
        main_page.click_to_button_place_order()
        main_page.open_order_feed_page()
        counter_value = order_feed_page.get_order_counter_for_entire_time()

        assert counter_value > initial_counter_value

    @allure.title("При создании заказа счетчик 'Выполнено за сегодня' увеличивается")
    def test_order_counter_for_day(self, login_user):
        main_page = MainPage(login_user)
        order_feed_page = OrderFeedPage(login_user)
        main_page.click_on_order_feed()
        initial_counter_value = order_feed_page.get_order_counter_for_day()
        main_page.click_button_constructor()
        main_page.wait_until_overlay_disappears()
        main_page.put_ingredient_into_basket()
        main_page.click_to_button_place_order()
        main_page.open_order_feed_page()
        counter_value = order_feed_page.get_order_counter_for_day()

        assert counter_value > initial_counter_value

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_number_order_in_progress(self, login_user):
        main_page = MainPage(login_user)
        order_feed_page = OrderFeedPage(login_user)
        main_page.put_ingredient_into_basket()
        main_page.click_to_button_place_order()
        main_page.wait_until_overlay_disappears()
        number_order = order_feed_page.get_number_order()
        main_page.open_order_feed_page()
        number_order_in_progress = order_feed_page.get_number_order_in_progress()

        assert number_order in number_order_in_progress
