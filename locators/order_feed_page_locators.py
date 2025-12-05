from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    BUTTON_CLOSE_ORDER_NUMBER = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]",
    )  # Кнопка закрытия окна номер заказа

    NUMBER_ORDER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]",
    )  # Номер заказа

    ORDER_COUNTER_FOR_ENTIRE_TIME = (
        By.XPATH,
        "//div[@class='undefined mb-15']/p[contains(@class, 'OrderFeed_number__2MbrQ text text_type_digits-large')]",
    )  # Счетчик "Выполнено за все время"

    COUNTER_ORDER_FOR_DAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )  # Счетчик "Выполнено за сегодня"

    NUMBER_ORDER_IN_PROGRESS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]/li[contains(@class, 'text text_type_digits-default mb-2')]",
    )  # Номер заказа в разделе "В работе"
