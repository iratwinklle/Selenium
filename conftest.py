import pytest

from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
   # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('twinkle88@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('888234190')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()


    yield

    pytest.driver.quit()


#
# @pytest.fixture
# def firefox_options(firefox_options):
#     firefox_options.binary = '/path/to/firefox-bin' #это путь к exe-драйверу Firefox
#     firefox_options.add_argument('-foreground') #возможность запуска в фоновом или реальном режиме.
#     # В нашем случае выбран последний. Для фонового укажите ‘-background’.
#     firefox_options.set_preference('browser.anchor_color', '#FF0000') # выбор цвета подложки браузера.
#     return firefox_options
#
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.binary_location = '/path/to/chrome' #путь к exe браузера (включая сам исполняемый файл).
#     chrome_options.add_extension('/path/to/extension.crx') #включение дополнений браузера.
#     chrome_options.add_argument('--kiosk')
#     return chrome_options
#
#
# #Для Chrome существует несколько фикстур, значительно расширяющих работу с драйвером.
# # Например, мы можем добавить уровень логирования для более сложных тестовых сценариев (debug):
# @pytest.fixture
# def driver_args():
#     return ['--log-level=LEVEL']
#
# #режимом запуска без пользовательского интерфейса, с так называемым headless-режимом («без головы»)
# import pytest
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.set_headless(True)
#     return chrome_options
#
# #content of file conftest.py
#
# import pytest
# import uuid
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # This function helps to detect that some test failed
#     # and pass this information to teardown:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
# @pytest.fixture
# def web_browser(request, selenium):
#
#     browser = selenium
#     browser.set_window_size(1400, 1000)
#
#     # Return browser instance to test case:
#     yield browser
#
#     # Do teardown (this code will be executed after each test):
#
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#
#             # Make screen-shot for local debug:
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#
#             # For happy debugging:
#             print('URL: ', browser.current_url)
#             print('Browser logs:')
#             for log in browser.get_log('browser'):
#                 print(log)
#
#         except:
#             pass # just ignore any errors here
# #
# #
