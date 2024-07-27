from utils.Weather import weather
from utils.NewData import writeNewDate, showData
from utils.Security import parserPost, searchPost
from utils.SearchInfo import info
from utils.Wiki import Wiki
import requests

description = """
На данный момент я могу:
	Узнать погоду: погода
	Сделать новую запись: --w
	Показать ваши записи: --r
	Собрать посты с securitylab: --s
	Искать информацию по собранным постам(не совсем доработано): search
	Искать информацию в Wiki: wiki
"""

def main():
	try:
		print(description)
		mini_ai = input('Какой запрос хотите сделать? ')
		mini_ai = mini_ai.lower()
		if 'погод' in mini_ai:
			weather()
		if '--w' in mini_ai:
			writeNewDate()
		if '--r' in mini_ai:
			showData()
		if '--s' in mini_ai:
			parserPost()
		if 'search' in mini_ai:
			info()
		if 'wiki' in mini_ai:
			Wiki()
	except KeyboardInterrupt:
		print('\nВыход из программы')
	except FileNotFoundError:
		print('\nФайл для чтений/записи не найден')
	except UnicodeDecodeError:
		print('\nНекорректный ввод')
	except requests.exceptions.ConnectionError:
		print('\nПроверьте подключение к сети')



main()