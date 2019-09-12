
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import sys
import csv
import sqlite3


def db_to_csv(filename):
    con = sqlite3.connect('d:\python\weather\weather.db')
    with con:
        cur = con.cursor()
        cur.execute("select * from Погода;")

    with open("d:\python\weather\{}.csv".format(filename), "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  #write headers
        csv_writer.writerows(cur)
    with open("d:\python\weather\{}.csv".format(sys.argv[2]), "r") as csv_file:
        dates = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for row in dates:
            print(','.join(row))


def check_city(city):
    con = sqlite3.connect('d:\python\weather\weather.db')
    with con:
        cur = con.cursor()
        cur.execute("select * from Погода;")

    with open("d:\python\weather\{}.csv".format(sys.argv[2]), "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  #write headers
        csv_writer.writerows(cur)
    with open('d:\python\weather\{}.csv'.format(sys.argv[2]), 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        city_id = []
        for row in reader:
            city_id.append(row['Город'])
        if city in city_id:
            weather_city(city)
        else:
            print('Указанного города нет в списке')


def weather_city(city):
    with open('d:\python\weather\weather.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Город'] == city:
                print('Город: {}, ' ' ДАТА: {}, ' ' Температура днем: {}, ' ' Температура ночью: {}'
                      .format(row['Город'], row['Дата'], row['Температура_днем'], row['Температура_ночью']))
            else:
                continue


def main():
    if len(sys.argv) != 4:
        print('usage: python export_weather.py {--csv | --city} file city')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    city = sys.argv[3]
    if option == '--csv':
        db_to_csv(filename)

    elif option == '--city':
        check_city(city)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()