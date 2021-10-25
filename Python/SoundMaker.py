from gtts import gTTS

myText = "Fogão ligado, temperatura 5"

language = 'pt'

saida = gTTS(text=myText, lang=language, slow=False)

saida.save("../LigaFogao.mp3")

