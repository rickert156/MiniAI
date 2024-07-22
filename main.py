from utils.Weather import weather
from utils.NewData import writeNewDate, showData

def main():
	mini_ai = input('Что-то хотите спросить? ')
	mini_ai = mini_ai.lower()
	if 'погод' in mini_ai:
		weather()
	if 'как ' in mini_ai and 'дела' in mini_ai:
		print('У меня все хорошо, у тебя как? ')
		input('')
	if 'сделать запись' in mini_ai:
		writeNewDate()
	if 'покажи запис' in mini_ai:
		showData()

main()