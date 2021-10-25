import cv2
import mediapipe as mp
from pygame import mixer
import threading
import time


class teste():
    results = None

'''Função que chama o Áudio de alerta'''
def PlayAlerts(caminho):
    mixer.init()
    mixer.music.load(caminho)
    mixer.music.play()
    time.sleep(3)




# aqui pega a Webcam para usar
cap = cv2.VideoCapture(0)

# chama a biblioteca de soluções e instancia mpHands
mpHands = mp.solutions.hands

# chama a função que define o padrão de captura da mão
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

'''Função que faz a captura da imagem trata, faz o tracking da mão e exibe'''
def Caption():
    count = 0
    while True:
        conectado, img = cap.read()

        # tranforma a imagem capturada em RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        teste.results = hands.process(imgRGB)
        # print(type(results.multi_hand_landmarks))

        # t2.start()
        # PlayAlerts(r'Sounds/Aviso1.mp3')

        # Verifica se está capturando e enquanto captura a mão que está sendo passado no for ele cria o landmark também
        if teste.results.multi_hand_landmarks:
            for handLms in teste.results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

'''
    Valida se está capturando/tracking a mão, e ativa por um momento, posteriormente se continuar a captura ele
    só ativará novamente o alerta se a mão sair da captura e voltar novamente
'''
def validaCaptura():
    count =0
    while True:
        ''' Aqui ele valida se está pegando algo, se estiver ele aciona o primeiro comando de faz um validação
                se ainda está capturando, se sim ele não repete o áudio até parar de capturar e começar novamente
            Ele não capturando exibe o aviso que não está capturando'''
        if teste.results:
            if not isinstance(teste.results.multi_hand_landmarks, type(None)):
                '''Inicia uma thread e passa o áudio'''
                count += 1
                threading.Thread(target=PlayAlerts(r'Sounds/Aviso5.mp3')).start()
                while not isinstance(teste.results.multi_hand_landmarks, type(None)):
                    print('pegando')
                    if isinstance(teste.results.multi_hand_landmarks, type(None)):
                        print('nao pegando')
                        break
            else:
                print('Não está capturando')


threading.Thread(target=validaCaptura).start()
Caption()

cap.release()
cv2.destroyAllWindows()
 