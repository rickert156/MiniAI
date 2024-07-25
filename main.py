from utils.Weather import weather
from utils.NewData import writeNewDate, showData
from utils.Security import securityLink, parserPost, searchPost
from utils.SearchInfo import info

def main():
	mini_ai = input('Что-то хотите спросить?(--w новая запись --r читать записи) ')
	mini_ai = mini_ai.lower()
	if 'погод' in mini_ai:
		weather()
	if '--w' in mini_ai:
		writeNewDate()
	if '--r' in mini_ai:
		showData()
	if '--s' in mini_ai:
		# securityLink()
		parserPost()
	if 'search' in mini_ai:
		info()


main()