# Importamos las bibliotecas necesarias
import RPi.GPIO as GPIO  # Para controlar los pines GPIO de la Raspberry Pi
import tkinter as tk  # Para crear la interfaz gráfica
from gpiozero import LED  # Para manejar LEDs de forma más sencilla

# Configuración de pines GPIO
signal_sensor_hw038 = 26  # Pin GPIO26 conectado al sensor HW-038
red = LED(14)  # Pin GPIO14 conectado al LED rojo
green = LED(17)  # Pin GPIO17 conectado al LED verde
BuzzerPin = 15  # Pin GPIO15 conectado al buzzer

# Configuramos el modo de numeración de pines (BCM = números GPIO)
GPIO.setmode(GPIO.BCM)

# Configuramos el pin del sensor HW-038 como entrada
GPIO.setup(signal_sensor_hw038, GPIO.IN)

# Configuramos el pin del buzzer como salida
GPIO.setup(BuzzerPin, GPIO.OUT)

# Configuración de la ventana principal de Tkinter
root = tk.Tk()  # Creamos la ventana principal
root.title("Sistema de detección de agua")  # Título de la ventana
root.geometry("500x500")  # Dimensiones de la ventana
root.resizable(False, False)  # Desactivamos la posibilidad de redimensionar la ventana

# Creamos un marco centrado para organizar el contenido dentro de la ventana
center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor="center")  # Lo centramos en la ventana

# Creamos una etiqueta para mostrar el estado del sensor
status_label = tk.Label(center_frame, text="Esperando...", font=("Arial", 18))
status_label.pack()  # Empaquetamos la etiqueta en el marco centrado

# Mensaje de inicio en la terminal
print("Iniciando lectura del nivel de agua...")

# Función para actualizar el fondo de la ventana y el estado de los dispositivos
def update_background(): 
    sensor_state = GPIO.input(signal_sensor_hw038)  # Leemos el estado del sensor
    if sensor_state == GPIO.HIGH:  # Si detecta agua (nivel estable)
        green.on()  # Encendemos el LED verde
        red.off()  # Apagamos el LED rojo
        GPIO.output(BuzzerPin, GPIO.LOW)  # Apagamos el buzzer
        print("Estado del nivel del agua: NIVEL ESTABLE")  # Mostramos el estado en la terminal
        root.configure(bg="green")  # Cambiamos el fondo de la ventana a verde
        status_label.config(text="Agua detectada", bg="green", fg="white")  # Actualizamos la etiqueta
    else:  # Si no detecta agua (nivel crítico)
        red.on()  # Encendemos el LED rojo
        green.off()  # Apagamos el LED verde
        GPIO.output(BuzzerPin, GPIO.HIGH)  # Encendemos el buzzer
        print("Estado del nivel del agua: ¡NIVEL CRITICO, ES NECESARIO REABASTECER!")  # Mensaje en la terminal
        root.configure(bg="red")  # Cambiamos el fondo de la ventana a rojo
        status_label.config(text="No se ha detectado agua", bg="red", fg="white")  # Actualizamos la etiqueta
    
    # Programamos la próxima actualización en 500 ms
    root.after(500, update_background)

# Iniciamos la primera actualización del fondo
update_background()

# Manejo del cierre del programa
try:
    root.mainloop()  # Inicia el bucle principal de la ventana
    
except KeyboardInterrupt:  # Excepción para interrupción del teclado (Ctrl+C)
    print("Programa interrumpido.")  # Mensaje en la terminal al finalizar
    red.off()  # Apagamos el LED rojo
    green.off()  # Apagamos el LED verde
    root.destroy()  # Cerramos la ventana
    GPIO.cleanup()  # Limpieza de los pines GPIO
