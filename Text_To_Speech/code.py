from gtts import gTTS


def convert_text_to_speech(text):
	#Default
	#tts = gTTS(text, lang='en')

	##Audio in English(Australia)
	#tts = gTTS(text, lang='en', tld='com.au')

	#Audio in English(India)
	tts = gTTS(text, lang='en', tld='co.in')

	tts.save('audio.mp3')

if __name__ == '__main__':
	text = input('Enter the Text: ')
	convert_text_to_speech(text)
	