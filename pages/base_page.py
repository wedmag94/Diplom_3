import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Подождать пока элемент станет невидимым")
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator):
        return self.wait_for_element(locator)

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Подождать кликабельности элемента")
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'nearest'});", element
        )

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        self.scroll_to_element(locator)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Получить текущий url")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Открыть страницу")
    def open_page(self, url):
        self.driver.get(url)

    # @allure.step("Ожидаем загрузку страницы")
