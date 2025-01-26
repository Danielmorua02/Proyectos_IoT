Este programa monitorea un sensor de nivel de agua (HW-038) conectado a una Raspberry Pi y muestra su estado en una ventana gráfica. 
Dependiendo de si se detecta agua o no:

    Si hay agua detectada:

        Se enciende un LED verde.
        Se apaga el LED rojo y el buzzer.
        La ventana muestra un fondo verde con el mensaje "Agua detectada".

    Si no se detecta agua:

        Se enciende un LED rojo.
        Se activa el buzzer.
        La ventana muestra un fondo rojo con el mensaje "No se ha detectado agua".
        El estado del sensor se actualiza cada 500 ms, y al cerrar el programa, se apagan los LEDs y se libera el control de los pines GPIO.

Para mas aclaracion puedes encontrar un video demostracion en el siguiente enlace:
    https://drive.google.com/file/d/1ZW-vYNURqb_nfqolZbvtbPI5da6-jodi/view?usp=sharing