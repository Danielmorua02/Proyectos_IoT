from gpiozero import LED #importamos la funcion LED del modulo gpiozero
from gpiozero import DistanceSensor #importamos la funcion DistanceSensor del modulo gpiozero
import time #importamos el modulo time

sensor = DistanceSensor(echo = 18, trigger = 22) #Creacion de variable "sensor" asignandole los datos de entrada del sensor Hc-sr04 asignandole los pines gpio 18 y 22
red = LED(14) #Asignamos el pin gpio 14 al led rojo
yellow = LED(15) #Asignamos el pin gpio 15 al led amarillo
green = LED(17) #Asignamos el pin gpio 17 al led verde

try: #Inicio de excepcion para la interrupcion de teclado
    while True: #inicializacion de bucle infinito
        distance =sensor.distance * 100 #Distancia en centimetros (*10 en decimetros, *1 en metros)
        print("Distancia : ", distance) #Imprimir en consola la distancia que esta detectando el sensor
        if distance < 10: #Condicion para encender el led rojo en caso de detectar un objeto a menos de 10 centimetros
            green.off()
            yellow.off()
            red.on()
        elif distance > 10 and distance < 25: #Condicion para encender el led amarillo en caso de detectar un objeto a entre 10 y 25 centimetros
            green.off()
            red.off()
            yellow.on()
        elif distance > 24 and distance < 40: #Condicion para encender el led verde en caso de detectar un objeto a entre 24 y 40 centimetros
            red.off()
            yellow.off()
            green.on()
        else: #Condicion para apagarlos tres leds simultaneamente en caso de no detectar un objeto a una distancia menor a 40 centimetros
            red.off()
            yellow.off()
            green.off()
            
        time.sleep(0.5) #pausa de medio segundo entre cada iteracion

except KeyboardInterrupt: #Excepcion detectada con interrupcion de teclado
    print("Programa interrumpido.") #Imprimir mensaje que el prorama fue interrumpido