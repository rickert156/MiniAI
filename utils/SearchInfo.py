from utils.Security import data, result, date_row, title_row, message_row
from utils.location import ipAddress
import csv


def info():
	query = 'Запрос постов Security'
	request = input('Что вы хотите найти? \n')
	space = '-'*20
	ipAddress(query)
	with open(f'{data}/{result}', 'r') as file:
		number_response=0
		for row in csv.DictReader(file):
			search = row[message_row]
			if request in search:
				number_response+=1
				print(f'[\t{number_response}\t]\n {search}\n{space}\n\n')
