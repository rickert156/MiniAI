import requests
import csv
from bs4 import BeautifulSoup
from utils.NewData import createDateDir

data = 'Data'
links_list = 'base.txt'
result = 'security.csv'
site = 'https://www.securitylab.ru'
date_row = 'Date'
title_row = 'Title'
message_row = 'News'

def postSave(date, title, post):
	with open(f'{data}/{result}', 'a+') as file:
		write = csv.DictWriter(file, fieldnames=[date_row, title_row, message_row])
		write.writerow({date_row:date, title_row:title, message_row:post})


def postRequest(link):
	response = requests.get(f'https://www.securitylab.ru{link}')
	response = response.text
	bs = BeautifulSoup(response, 'lxml')
	try:
		date = bs.find('time').get_text()
	except:data = 'none'
	try:
		title = bs.find('h1').get_text()
	except:title = 'none'
	try:
		post = bs.find('sape_index').get_text()
		post = ' '.join(post.split())
	except:post = 'none'
	try:
		print(f'{date}\n{title}\n{post}')
		postSave(date, title, post)
	except:print('При записи произошла ошибка')

def parserPost():
	with open(f'{data}/{links_list}', 'r') as file:
		number_string=0
		for link in file.readlines():
			number_string+=1
			link = link.strip()
			postRequest(link)
			print(f'[{number_string}] Собрал данные с {site}{link}\n')

def searchPost(response):
	createDateDir()
	bs = BeautifulSoup(response, 'lxml')
	base = f'{data}/{links_list}'
	for links in bs.find_all('a'):
		href = links.get('href')
		if href and '/news/' in href and 'php' in href:
			print(href)
			with open(base, 'a+') as file:
				file.write(f'{href}\n')

	print('-'*20)

def securityLink():
	pages = 'https://www.securitylab.ru/news/page1_'
	number_requests = 0
	while number_requests <= 4403:
		number_requests+=1
		site = f'{pages}{number_requests}.php'
		response = requests.get(site)
		response = response.text
		print(f'[{number_requests}] {site}')
		searchPost(response)



