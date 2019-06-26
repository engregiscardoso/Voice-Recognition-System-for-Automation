import time
import Base
import RPi.GPIO as GPIO
from Base import LerEntrada 
from Base import Conectar 

while True:
    value = LerEntrada.entrada_voz()
    valueNew = LerEntrada.tratar_entrada(value) 
   
    while True:
        if valueNew[0] == "ligar":
            if len(valueNew) == 2 and valueNew[1] == "arcondicionado":
                print("Ar condicionado ligado")

            elif len(valueNew) == 2 and valueNew[1] == "televisão":
                Conectar.chama_msg()
                print("Televisão ligada")
                
            elif len(valueNew) == 2 and valueNew[1] == ("lâmpada" or "lampada"):
                if len(valueNew) == 3 and valueNew[2] == ("sala"):
                    GPIO.output(5, GPIO.HIGH)
                    print("Lâmpada da sala ligada")
                    break
                        
                elif len(valueNew) == 3 and valueNew[2] == "cozinha":
                    GPIO.output(6, GPIO.HIGH)
                    print("Lâmpada da cozinha ligada")
                    break
                else:
                    break
                
            else:
                break

        elif valueNew[0] == "desligar":
            if len(valueNew) == 2 and valueNew[1] == "ar":
                print("Desligou o Ar condicionado")
            
            elif len(valueNew) == 2 and valueNew[1] == "televisão":
                print("Televisão desligada")
            
            elif len(valueNew) == 2 and valueNew[1] == ("lâmpada" or "lampada"):
                if len(valueNew) == 3 and valueNew[2] == ("sala"):
                    GPIO.output(5, GPIO.LOW)
                    print("Lâmpada da sala desligada")
                    break
                        
                elif len(valueNew) == 3 and valueNew[2] == "cozinha":
                    GPIO.output(6, GPIO.LOW)
                    print("Lâmpada da cozinha desligada")
                    break
                else:
                    break
               
            else:
                break
        else:
            print("Comando não encontrado")
            break
        

