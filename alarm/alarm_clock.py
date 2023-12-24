from tkinter import *
import datetime
# from time import strftime
from threading import *
import pygame
from pygame import mixer
import time
import sys

# Inicialize o pygame e o mixer
pygame.init()
pygame.mixer.init()

# create object
root = Tk()
root.bind('<Control-c>', quit)
root.geometry("300x250")
root.resizable(False, False)  # Tornando a janela não redimensionável

# Create a StringVar for countdown
countdown_var = StringVar()

# Label to display countdown
countdown_label = Label(root, textvariable=countdown_var, font="Helvetica 15", fg="red")
countdown_label.place(x=155, y=5)

# Global variable to control alarm
alarm_on = False
set_alarm_time = "00:00:00"

def update_time():
    global alarm_on, set_alarm_time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clockTime.config(text=current_time)
    if alarm_on and set_alarm_time is not None:
        time_left = datetime.datetime.strptime(set_alarm_time, "%H:%M:%S") - datetime.datetime.strptime(current_time, "%H:%M:%S")
        if time_left.total_seconds() < 0:  # Verifica se time_left é negativo
            time_left = datetime.timedelta(seconds=0)  # Se for, define time_left como 0
        sys.stdout.write("\r" + str(time_left))
        sys.stdout.flush()
        countdown_var.set(str(time_left))
        if time_left.total_seconds() <= 10:  # Se faltarem 10 segundos ou menos, muda a cor do texto para vermelho
            countdown_label.config(fg="red")
        else:  # Caso contrário, mantém a cor do texto como preta
            countdown_label.config(fg="gray")
    clockTime.after(1000, update_time)



def alarm():
    global alarm_on, set_alarm_time
    while alarm_on:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time > set_alarm_time:
            sys.stdout.write("\rTime is up!")
            sys.stdout.flush()
            mixer.init()
            mixer.music.load("sound.wav")
            mixer.music.play(-1)  # O argumento -1 faz a música tocar em ‘loop’
            while alarm_on:  # Este ‘loop’ mantém a música tocando até que alarm_on seja False
                time.sleep(1)
            break
        time.sleep(1)


def threading():
    global alarm_on, set_alarm_time
    alarm_on = True
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    t1 = Thread(target=alarm)
    t1.start()
    alarm_button.config(text="Stop Alarm", command=stop_alarm)  # Update the button immediately after setting the alarm

def stop_alarm():
    global alarm_on
    alarm_on = False
    mixer.music.stop()
    alarm_button.config(text="Set Alarm", command=threading)  # Update the button back to "Set Alarm" after stopping the alarm

# Label to display time
clockTime = Label(root, font=("roboto", 20), foreground="black")
clockTime.place(x=90, y=180)

# Chamando a função time para começar a atualizar a exibição do tempo
update_time()

Label(root, text="Alarm", font="Helvetica 20 bold", fg="blue").place(x=60, y=0)
Label(root, text="set alarm below:", font="Helvetica 10 bold", fg="black").place(x=60, y=43)

frame = Frame(root)
frame.place(x=60, y=74)

hour = StringVar(root)
hours = tuple("{:02d}".format(i) for i in range(24))
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = tuple("{:02d}".format(i) for i in range(60))
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = tuple("{:02d}".format(i) for i in range(60))
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

alarm_button = Button(root, text="Set Alarm", font="Helvetica 15", fg="white", bg="blue", command=threading)
alarm_button.place(x=95, y=120)

try:
    # Iniciando o loop principal de eventos Tkinter
    root.mainloop()

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

