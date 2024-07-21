import csv, os

dataFile = 'data.csv'
dirDate = 'Data'
theme = 'Тема'
message = 'Данны'

def createDateDir():
	if not os.path.exists(dirDate):
		os.makedirs(dirDate)
		with open(f'{dirDate}/{dataFile}', 'a+', encoding='utf-8') as file:
			write = csv.writer(file)
			write.writerow([theme, message])

def writeNewDate():
	createDateDir()
	try:
		data_theme = input('Укажите тему: ')
		data_message = input('Укажите данные: ')
		with open(f'{dirDate}/{dataFile}', 'a+', encoding='utf-8') as file:
			write = csv.DictWriter(file, fieldnames=[theme, message])
			write.writerow({theme:data_theme, message:data_message})
	except UnicodeDecodeError:
		print('Возникла ошибка с кодировкой, попробуйте пожалуйста еще раз написать\n')
		writeNewDate()