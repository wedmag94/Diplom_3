## Дипломный проект. Задание 3: UI-тесты для Stellar Burgers
<hr>

## Студент: Лидия Чумбарева

## <h>Когорта: #32</h>
<hr>

## <h>Project: Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла                | Содержание файла                              |
|-------------------------------|-----------------------------------------------|
| locators dir                  | Директория с локаторами                       |
| main_page_locators.py         | Файл с локаторами главной страницы            |
| order_feed_page_locators.py   | Файл с локаторами страницы "Лента Заказов"    |
| pages dir                     | Директория PageObject                         |
| base_page.py                  | Базовый класс с общими методами               |
| main_page.py                  | Класс с методами главной страницы             |
| order_feed_page.py            | Класс с методами страницы "Лента Заказов"     |
| tests dir                     | Директория с тестами                          |
| test_main_page.py             | Тесты главной страницы                        |
| test_order_feed_page.py       | Тесты раздела "Лента Заказов"                 |
| conftest.py                   | Фикстуры                                      |
| data.py                       | Файл с тестовыми данными                      |
| curl.py                       | Файл с URL страниц                            |
| requirements.txt              | Файл с зависимостями                          |
| allure_results.dir            | Папка с отчетами Allure                       |

