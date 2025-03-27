# QA Python Sprint 6

## UI автотесты для сайта [Самокат](https://qa-scooter.praktikum-services.ru/)
## Структура проекта:

`locators/` _классы с локаторами для страниц_
 - `base_page_locators.py`
 - `main_page_locators.py`
 - `order_page_locators.py`
   
`pages/` _классы страниц с методами_
 - `base_page.py`
 - `main_page_py`
 - `order_page.py`
   
`tests/` _тестовые классы_
 - `test_logo_navigation.py`
 - `test_main_page.py`
 - `test_order_page.py`
   
`data.py` _тестовые данные выпадающего списка в разделе «Вопросы о важном»._

`urls.py` _URL-адреса_

`user_data.py` _тестовые данные для флоу позитивного сценария с двумя наборами данных._

`conftest.py` _фикстура драйвера Firefox_

`allure-results` _отсчеты о тестах_



Реализованы слудующие тестовые сценарии:
 - Проверка выпадающего списка в разделе "Вопросы о важном" на корректное отображение текста ответа.
 - Заказ самоката самоката с двумя наборами данных через кнопки "Заказать" в шапке и на главной странице.
 - Клик на логотип "Самокат"
 - Клик на логотип "Яндекс"
