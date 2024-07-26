import requests
from bs4 import BeautifulSoup
from utils.location import ipAddress

query = 'Запрос Погоды'


def weather():
	city = ipAddress(query)
	temp_day = 'Днем:'
	temp_evening = 'Вчером:'
	temp_night = 'Ночью:'

	params = city
	site = 'https://weather.rambler.ru/'

	respose = requests.get(site, params=params)
	respose = respose.text
	bs = BeautifulSoup(respose, 'lxml')
	city = bs.find(class_='rICO')
	temp = bs.find(class_='PQ4J')
	city, temp = city.get_text(), temp.get_text()
	print(f'\n{city}: {temp}\n{"-"*10}\nПримерный прогноз на сегодня:')
	number_iter = 0
	for temp_today in bs.find_all(class_='xNIt'):
		temp_today = temp_today.get_text()
		number_iter+=1
		if number_iter == 1:
			print(f'{temp_day} {temp_today}')
		elif number_iter == 2:
			print(f'{temp_evening} {temp_today}')
		elif number_iter == 3:
			print(f'{temp_night} {temp_today}')


	