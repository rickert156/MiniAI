import requests
from bs4 import BeautifulSoup

def Wiki():
	search = input('Что вы хотете найти в Вики? \n')
	wiki = 'https://ru.wikipedia.org/wiki/'
	response = requests.get(f'{wiki}{search}')
	response = response.text
	bs = BeautifulSoup(response, 'lxml')
	print(bs.body.get_text())
