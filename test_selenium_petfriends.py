#запустить тест pytest -v --driver Chrome --driver-path C:\Users\User\PycharmProjects\Selenium\chromedriver.exe test_selenium_petfriends.py
from collections import Counter

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

from selenium.webdriver.common.by import By

#Модуль 25.3.1
#проверка всех питомцев пользователя на наличие имени, вида и возраста на странице все питомцы

def test_show_my_pets():
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   # Нажимаем на кнопку перехода на страницу "Мои питомцы"
   pytest.driver.find_element_by_css_selector('html > body > nav > button > span').click()  # т.к. открывается маленькое
   # окно, нам надо щелкнуть на список, в котором будет ссылка на страницу "Мои питомцы"
   pytest.driver.find_element_by_css_selector('div#navbarNav > ul > li > a').click()
   # Проверяем, что мы оказались на  странице "Мои питомцы"
   assert pytest.driver.find_element_by_tag_name('h2').text == "Twinkle"

def test_check_my_pets():
   '''Проверить, что на странице "Мои питомцы" присуствуют все питомцы. По условиям задачи количество
   питомцев должно быть взято из статистики пользователя'''
   #заходим на страницу "Мои питомцы"
   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
   #Необходимо взять количество питомцев из статистики пользователя
   #сохраним в переменную  statistics все элементы статистики
   statistics = pytest.driver.find_elements_by_css_selector('.\\.col-sm-4.left')
   #Получаем количество питомцев из элементов статистики
   number_of_stat = statistics[0].text.split('\n')
   number_of_stat = number_of_stat[1].split(' ')
   number_of_stat = int(number_of_stat[1])
   # Убеждаемся, что мы добыли его верно
   print('Число питомцев из статистики пользователя:', number_of_stat)
   #посчитаем количество питомцев по одной из обязательных характеристик "Имя питомца".
   # Имя каждого из питомца лежит в теге td[1]
   number_of_names = len(pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]'))
   # Убеждаемся, что мы добыли его верно
   print('Число питомцев по числу имен:', number_of_names)
   assert number_of_stat == number_of_names


def test_pets_list_have_photo():
   '''Проверить, что на странице "Мои питомцы" хотя бы у половины питомцев есть фото. По условиям задачи количество
   питомцев с фото тоже можно посчитать, взяв статистику пользователя.
   Вопрос для самопроверки: Половина от чётного и нечётного количества фотографий выдаёт одинаковые результаты теста?'''
   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
   # Проверить, что на странице "Мои питомцы" присутствуют все питомцы
   # Из всей таблицы питомцев
   pets_list = pytest.driver.find_element_by_xpath("//tbody")
   # Определить количество всех питомцев на странице "Мои питомцы" по тегу img
   pets_list_photo = pets_list.find_elements_by_tag_name('img')
   # Посчитать кол-во тех питомцев, у которых значение абрибута scr в теге img не равно нулю, то есть есть ссылка на фото
   counter = 0
   for i in pets_list_photo:
      if i.get_attribute('src') != "":
         counter += 1
   # Проверить, что питомцев с фото больше либо равно половине всего списка питомцев с тегом img
   assert counter >= len(pets_list_photo) / 2, 'The page have NO pet`s photos'
   print('Общее число моих питомцев:{}. Количество питомцев с фотографией {}'.format(len(pets_list_photo), counter))


def test_pets_info_not_null():
   '''Проверить, что на странице "Мои питомцы" у всех питомцев есть имя, возраст и порода'''
   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
   # Проверить, что на странице "Мои питомцы" присутствуют все питомцы
   # Из всей таблицы питомцев
   pets_list = pytest.driver.find_element_by_xpath("//tbody")
   # Новый список питомцев
   each_pet = pets_list.find_elements_by_tag_name('tr')
   # Создать пустой список, куда будем помещать добытый циклом список элементов "Кличка", "Порода", "Возраст" для каждого питомца вперемешку
   pets_list_info = []
   for i in each_pet:
      pets_list_info.append(list(i.find_elements_by_tag_name('td')))
   # Циклом получившийся список разбить на отдельные элементы "Кличка", "Порода", "Возраст"
   bad_pet = False
   for i in pets_list_info:
      pet_name = i[0].text
      pet_kind = i[1].text
      pet_age = i[2].text
   # Если какой-то из этих элементов пуст, то прервать цикл
      if pet_name == "" or pet_kind == "" or pet_age == "":
         bad_pet == True
         break

   assert bad_pet == False


def test_only_unique_pet_names():
   '''Проверить, что на странице "Мои питомцы" у всех питомцев разные имена'''
   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
   # Проверить, что на странице "Мои питомцы" присутствуют все питомцы
   pets_list = pytest.driver.find_element_by_xpath("//tbody")
   each_pet = pets_list.find_elements_by_tag_name('tr')
   # Создать пустой список питомцев, куда с помощью цикла будем класть имена питомцев
   pet_names = []

   for i in each_pet:
      pet_names.append(i.find_element_by_tag_name('td').text)


   assert len(Counter(pet_names)) == len(each_pet)

def test_only_unique_pet_data():
   '''Проверить, что на странице "Мои питомцы" в списке нет повторяющихся питомцев'''
   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
   # Проверить, что на странице "Мои питомцы" присутствуют все питомцы
   pets_list = pytest.driver.find_element_by_xpath("//tbody")
   each_pet = pets_list.find_elements_by_tag_name('tr')

   pets_list_info = []
   for i in each_pet:
      separated_pets_attribute = i.find_elements_by_tag_name('td')
      name = separated_pets_attribute[0].text
      age = separated_pets_attribute[1].text
      kind = separated_pets_attribute[2].text

      pets_list_info.append(name+age+kind)

   print(Counter(pets_list_info))

   assert len(Counter(pets_list_info)) == len(pets_list_info)
