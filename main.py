'''
простой парсинг сайта фильмов https://w.mxfilm.es/filmy/komedija/
'''
import requests                 # это простые библиотеки для парсинга
from bs4 import BeautifulSoup   #
import pandas as pd             # библиотека для создания таблиц и csv файлов

mxfilm = []                                 # список куда будем записывать данные сайта фильмов
u  = 'https://w.mxfilm.es/filmy/komedija/'
r = requests.get(u)
s = BeautifulSoup(r.text, 'lxml')

for i in range(1,125):                      # проход по страницам сайта

    url = f'https://w.mxfilm.es/filmy/komedija/page/{i}/'
    r1 = requests.get(url)
    s1 = BeautifulSoup(r1.text, 'lxml')
    films = s1.findAll('div', class_='th-item')

    for film in films:                       # проход по всем одинаковым тегам 'div' с класом class_='th-title'

        name  = film.find('div', class_='th-title').text            #имя фильма
        year = film.find('div', class_='th-series').text            #год фильма
        rate = film.find('div', class_='th-rate th-rate-kp').text   #рейтинг
        if rate == '':                                              #условие если рейтинга нет
            rate = '- -'

        mxfilm.append([name, year, rate])                   #записываем список из имени,года выпуска и рейтинга
                                                                    #фильма в список mxfilm
kolonka = ['name', 'year', 'rate']                  #создаем название колонок таблицы
file = pd.DataFrame(mxfilm, columns=kolonka)        #показываем откуда  загружаем  данные файла
file.to_csv('films.csv', sep=';', encoding='utf8 ') #создаем его в самом проекте, декодим его и делаем шаг и
