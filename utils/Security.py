import requests
import csv
from bs4 import BeautifulSoup
from utils.NewData import createDateDir

def searchPost(response):
	createDateDir()
	data = 'Data'
	bs = BeautifulSoup(response, 'lxml')
	base = f'{data}/base.txt'
	for links in bs.find_all('a'):
		href = links.get('href')
		if href and '/news/' in href:
			if 'php' in href:
				print(href)
				with open(base, 'a+') as file:
					file.write(f'{href}\n')

	print('-'*20)

def dataPars(dates, title, subtitle):
	base = 'test.csv'
	with open(base, 'a+') as file:
		write = csv.DictWriter(file, fieldnames=['Date', 'Title', 'Description'])
		write.writerow({'Date':dates, 'Title':title, 'Description':subtitle})

def parser(response):
	bs = BeautifulSoup(response, 'lxml')
	date_post = bs.find_all('time')
	title_post = bs.find_all('h2')
	subtitle_post = bs.find_all('p')
	link_post = bs.find_all('a', class_='article-card.inline-card')

	for dates, title, subtitle in zip(date_post, title_post, subtitle_post):
		dates = dates.get_text()
		title = title.get_text()
		subtitle = subtitle.get_text()
		print(f'{dates} {title} {subtitle}')
		dataPars(dates, title, subtitle)

def security():
	pages = 'https://www.securitylab.ru/news/page1_'
	number_requests = 0
	while number_requests <= 4403:
		number_requests+=1
		site = f'{pages}{number_requests}.php'
		response = requests.get(site)
		response = response.text
		print(f'[{number_requests}] {site}')
		# parser(response)
		searchPost(response)



