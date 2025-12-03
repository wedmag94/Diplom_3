from selenium.webdriver.common.by import By


class MainPageLocators:

    OVERLAY = (
        By.XPATH,
        ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div",
    )

    CONSTRUCTOR_BOTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка Конструктор

    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']",
    )  # Кнопка Лента заказов

    INGREDIENT = (
        By.XPATH,
        "//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH')]",
    )

    WINDOW_DETAILS_INGREDIENT = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]",
    )  # Окно детали ингредиента

    CLOSING_WINDOW = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]",
    )  # Закрытие окна Детали ингредиента

    COUNTER_INGREDIENT = (
        By.XPATH,
        "//p[contains(@class, 'counter_counter__num__3nue1')]",
    )  # Счетчик ингредиента

    BASKET = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]",
    )  # Корзина

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']",
    )  # Кнопка Войти в аккаунт

    INPUT_EMAIL = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @type='text']",
    )  # Поле ввода Email

    INPUT_PASSWORD = (
        By.XPATH,
        "//input[@class ='text input__textfield text_type_main-default' and @type='password']",
    )  # Поле ввода Пароля

    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")

    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    WINDOW_NUMBER_ORDER = (By.XPATH, "//div[@class ='Modal_modal__container__Wo2l_']")
