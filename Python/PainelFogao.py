import serial
import threading
from pygame import mixer
import time

arduino = serial.Serial('COM3', 9600)
validaFogao = 0
TemperaturaFogao = 5
count = 0

def PlayAlerts(caminho):
    mixer.init()
    mixer.music.load(caminho)
    mixer.music.play()
    time.sleep(3)



def timezin():
    return str(arduino.readline())


while True:

    linha = str(arduino.readline())
    linhaInt = linha[2:-5]
    print(linhaInt)



    if linhaInt == "FogaoLigado" and validaFogao == 0:
        threading.Thread(target=PlayAlerts(r'LigaFogao.mp3')).start()
        validaFogao += 1
    elif linhaInt == "FogaoLigado" and validaFogao == 1:
        threading.Thread(target=PlayAlerts(r'DesligaFogaoSound.mp3')).start()
        validaFogao = 0


    '''if linhaInt == "Aumenta" and validaFogao != 0:
        threading.Thread(target=PlayAlerts(r'AumentaTemp.mp3')).start()

    if linhaInt == "Diminui" and validaFogao != 0:
        threading.Thread(target=PlayAlerts(r'DiminuiTemp.mp3')).start()'''

    if linhaInt == "Aumenta":
        if TemperaturaFogao == 5 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura6.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 6 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura7.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 7 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura8.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 8 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura9.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 9 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura10.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 4 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura5.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 3 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura4.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 2 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura3.mp3')).start()
            TemperaturaFogao += 1
        elif TemperaturaFogao == 1 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura2.mp3')).start()
            TemperaturaFogao += 1


    if linhaInt == "Diminui":
        if TemperaturaFogao == 2 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura1.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 3 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura2.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 4 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura3.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 5 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura4.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 6 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura5.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 7 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura6.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 8 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura7.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 9 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura8.mp3')).start()
            TemperaturaFogao -= 1
        if TemperaturaFogao == 10 and validaFogao != 0:
            threading.Thread(target=PlayAlerts(r'Temperatura9.mp3')).start()
            TemperaturaFogao -= 1

    if linhaInt == '12' or linhaInt == '11':
        # PlayAlerts(r'Aviso2.mp3')
        if not count == 1:
            threading.Thread(target=PlayAlerts(r'Aviso6.mp3')).start()
            count += 1
            print("Captou panela")
        linha = str(arduino.readline())
        linhaInt = linha[2:-5]
        print(linhaInt)



arduino.close()
