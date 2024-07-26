import requests, time
from bs4 import BeautifulSoup

def dataWrite(date, ip, city, query):
	data_file = 'log.txt'

	with open(data_file, 'a+') as file:
		data = file.write(f'{date}, {ip} {city}\t| {query}\n')

def ipAddress(query):
	date = time.strftime('%d.%m.%Y %H:%M:%S')
	respose = requests.get('https://2ip.ru/')
	respose = respose.text
	bs = BeautifulSoup(respose, 'lxml')
	ip = bs.find(class_='ip')
	city = bs.find(id='ip-info-country')

	ip, city = ip.get_text(), city.get_text()
	ip = ip.split()
	city = city.split(',')[0].strip()

	dataWrite(date, ip, city, query)