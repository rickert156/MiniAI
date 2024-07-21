from utils.Weather import weather

def main():
	mini_ai = input('Что-то хотите спросить? \n')
	mini_ai = mini_ai.lower()
	if 'погод' in mini_ai:
		weather()
	if 'как ' in mini_ai and 'дела' in mini_ai:
		print('У меня все хорошо, у тебя как? \n')
		input('')

main()