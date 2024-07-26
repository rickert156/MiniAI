import requests
from bs4 import BeautifulSoup
from utils.location import ipAddress

def Wiki():
	query = 'Запрос Wiki'
	search = input('Что вы хотете найти в Вики? \n')
	wiki = 'https://ru.wikipedia.org/wiki/'
	response = requests.get(f'{wiki}{search}')
	response = response.text
	bs = BeautifulSoup(response, 'lxml')
	title = bs.title.get_text()
	body = bs.find(id='bodyContent').get_text()
	ipAddress(query)
	if 'В Википедии нет статьи с таким названием.' in body:
		title = 'Отсутствует'
		body = 'В Википедии нет статьи с таким названием.'
	print(f'\nЗаголовок страницы: {title}\n{body}')
