import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import speech_recognition as sr
import string
import nltk
from nltk.corpus import stopwords

GPIO.setwarnings(False)

broker = "iot.eclipse.org"
#define callback
client = paho.Client() 

class Conectar():
    
    """Esta classe realiza a conexão."""
         
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)

            
    def on_message(client, userdata, message):
        time.sleep(1)
        print("received message =",str(message.payload.decode("utf-8")))

    
    def chama_msg():
        print("connecting to broker ",broker)
        client.connect(broker)#connect
        client.loop_start() #start loop to process received messages
        print("subscribing ")
        client.publish("inTopicregis","1")
        client.subscribe("outTopicregis")
        client.on_message=on_message


class LerEntrada:

    #Habilita o microfone para ouvir o usuario
    def entrada_voz():
        while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                        #Chama a funcao de reducao de ruido disponivel na speech_recognition
                        r.adjust_for_ambient_noise(source)
                        #Avisa ao usuario que esta pronto para ouvir
                        print("Esperando comando de voz: ")
                        #Armazena a informacao de audio na variavel
                        audio = r.listen(source)
                
                try:
                        #Passa o audio para o reconhecedor de padroes do speech_recognition
                        messagereceive = r.recognize_google(audio,language='pt-BR')
                        #Após alguns segundos, retorna a frase falada
                        print("Você disse: " + messagereceive)
                        return messagereceive

                #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
                except:
                        print("Não Compreendi")
                        

    def tratar_entrada(messagereceive):
        #messagereceive = 'Desligar a lampada da sala'
        messagereceive = messagereceive.lower()

        #Separação letra por letra
        sempont = [car for car in messagereceive if car not in string.punctuation]

        sempont=''.join(sempont)

        #Remoção stopwords
        stopwords.words('portuguese')

        #Tokenização
        clean_mess = [word for word in sempont.split() if word.lower() not in stopwords.words('portuguese')]
           
        return clean_mess














