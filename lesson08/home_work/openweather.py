
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import os
import sqlite3 as lite
import urllib.request
from xml.etree import ElementTree as ET


class Weather(object):
    def url_request(self, city_id):
        while True:
            try:
                urllib.request.urlretrieve('http://export.yandex.ru/weather-ng/forecasts/{}.xml'.format(city_id),
                                           'd:/python/weather/{}.xml'.format(city_id))
                break
            except:
                continue

    def day_date(self, city_id):
        f = open('d:/python/weather/{}.xml'.format(city_id), 'r')
        forecast = f.read()
        root = ET.fromstring(forecast)
        date = root.find('.//{http://weather.yandex.ru/forecast}day').attrib
        return date['date']

    def night_short(self, city_id):
        f = open('d:/python/weather/{}.xml'.format(city_id), 'r')
        forecast = f.read()
        root = ET.fromstring(forecast)
        temperature = root.find('.//{http://weather.yandex.ru/forecast}day_part[@type="night_short"]/').text
        return temperature

    def day_short(self, city_id):
        f = open('d:/python/weather/{}.xml'.format(city_id), 'r')
        forecast = f.read()
        root = ET.fromstring(forecast)
        temperature = root.find('.//{http://weather.yandex.ru/forecast}day_part[@type="day_short"]/').text
        return temperature


def create_table():
    con = lite.connect('d:/python/weather/weather.db')
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Погода
                   (Id INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE,
                    Температура_днем INTEGER, Температура_ночью INTEGER )""")

    if not os.path.exists('d:/python/weather/cities.db'):
        urllib.request.urlretrieve('http://weather.yandex.ru/static/cities.xml', 'd:/python/weather/cities.xml')
    tree = ET.parse('d:/python/weather/cities.xml')
    root = tree.getroot()
    list_city = []

    for child in root:
        list_city.append(child.attrib['name'])
        print('--->', child.attrib['name'])

    s = True
    weather = Weather()
    while s == True:
        country_id = input('Выбирете страну из списка и введите название или введите quit для выхода из программы:')
        if country_id in list_city:
            for country in root.findall('country'):
                if country.get('name') == country_id:
                    for city in country.iter('city'):
                        weather.url_request(city.get('id'))
                        id_city = [city.get('id'), city.text, weather.day_date(city.get('id')),
                                   weather.day_short(city.get('id')), weather.night_short(city.get('id'))]
                        con = lite.connect('.')
                        print(id_city)
                        try:
                            with con:
                                cur = con.cursor()
                                cur.execute("INSERT INTO Погода VALUES (?,?,?,?,? );", id_city)
                                con.commit()
                        except:
                            with con:
                                cur = con.cursor()
                                cur.execute("UPDATE  Погода SET  Дата=? WHERE ID=?",
                                            (weather.day_date(city.get('id')), city.get('id')))
                                cur.execute("UPDATE Погода SET Температура_днем=? WHERE ID=?",
                                            (weather.day_short(city.get('id')), city.get('id')))
                                cur.execute("UPDATE Погода SET Температура_ночью=? WHERE ID=?",
                                            (weather.night_short(city.get('id')), city.get('id')))
                                con.commit()

            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Погода")
                rows = cur.fetchall()

            for row in rows:
                print(row)
            s = False

        elif country_id == 'quit':
                break
        else:
            print('Введите страну из списка или quit для выхода из программы! :')


if __name__ == '__main__':
    create_table()
