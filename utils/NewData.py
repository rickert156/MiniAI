import csv, os, time

dataFile = 'data.csv'
dirDate = 'Data'
theme = 'Тема'
message = 'Данные'

def showData():
	with open(f'{dirDate}/{dataFile}', 'r') as file:
		number_string=0
		for row in csv.DictReader(file):
			number_string+=1
			theme_row = row[theme]
			message_row = row[message]
			print(f'[{number_string}] {theme_row}\n{message_row}\n')


def createDateDir():
	if not os.path.exists(dirDate):
		os.makedirs(dirDate)
		with open(f'{dirDate}/{dataFile}', 'a+', encoding='utf-8') as file:
			write = csv.writer(file)
			write.writerow([theme, message])

def writeNewDate():
	createDateDir()
	try:
		data_file = 'log.txt'

		data_theme = input('Укажите тему: ')
		data_message = input('Укажите данные: ')
		with open(f'{dirDate}/{dataFile}', 'a+', encoding='utf-8') as file:
			write = csv.DictWriter(file, fieldnames=[theme, message])
			write.writerow({theme:data_theme, message:data_message})

			date = time.strftime('%d.%m.%Y %H:%M:%S')
			with open(data_file, 'a+') as file:
				data = file.write(f'{date}\tЗапись новых данных в тему: "{data_theme}"\n')
		
	except UnicodeDecodeError:
		print('Возникла ошибка с кодировкой, попробуйте пожалуйста еще раз написать\n')
		writeNewDate()