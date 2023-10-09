from gpiozero import TrafficLights, Button, Buzzer
import time
import signal
from time import sleep
from signal import pause


# Traffic lights for cars
car_lights = TrafficLights( # Assuming GPIO pins:
        4,  # (red)
        12, # (amber)
        21  # (green)
        )


# Traffic lights for pedestrians
pedestrian_lights = TrafficLights( # Assuming GPIO pins:
        6,  # (red)
        13, # (amber) (for sound)
        19  # (green)
        )


# Button for pedestrians
pedestrian_button = Button(22)  # Assuming GPIO pin 25 for the button




# Control + c handler
def handler(signum, frame):
    res = input(" \n<Control-c> was pressed. \nDo you really want to stop Traffic Ligh process?. y/n: ")
    if  res == 'y':
        exit(1)


# Mode stop_car
def car_stop_mode():
    car_lights.red.off()
    car_lights.amber.off()
    car_lights.green.on()
    pedestrian_lights.red.on()
    sleep(5)
    car_lights.red.off()
    car_lights.amber.on()
    car_lights.green.off()
    sleep(1)
    car_lights.red.on()
    car_lights.amber.off()
    car_lights.green.off()
    sleep(1)


def pedestrian_pass_normal_mode():
    timenow = time.time()
    newtime = 0
    while newtime < 5:
        pedestrian_lights.red.off()
        pedestrian_lights.green.on()
        pedestrian_lights.amber.on()
        sleep(1)
        pedestrian_lights.red.off()
        pedestrian_lights.green.off()
        pedestrian_lights.amber.off()
        sleep(1)
        newtime = time.time() - timenow


def pedestrian_pass_normal_mode():
    timenow = time.time()
    newtime = 0
    while newtime < 5:
        pedestrian_lights.red.off()
        pedestrian_lights.green.on()
        pedestrian_lights.amber.on()
        sleep(1)
        pedestrian_lights.red.off()
        pedestrian_lights.green.off()
        pedestrian_lights.amber.off()
        sleep(1)
        newtime = time.time() - timenow


def pedestrian_pass_fast_mode():
    timenow = time.time()
    newtime = 0
    while newtime < 5:
        pedestrian_lights.red.off()
        pedestrian_lights.green.on()
        pedestrian_lights.amber.on()
        sleep(0.5)
        pedestrian_lights.red.off()
        pedestrian_lights.green.off()
        pedestrian_lights.amber.off()
        sleep(0.5)
        newtime = time.time() - timenow


def pedestrian_pass_ultrafast_mode():
    timenow = time.time()
    newtime = 0
    while newtime < 3:
        pedestrian_lights.red.off()
        pedestrian_lights.green.on()
        pedestrian_lights.amber.on()
        sleep(0.1)
        pedestrian_lights.red.off()
        pedestrian_lights.green.off()
        pedestrian_lights.amber.off()
        sleep(0.1)
        newtime = time.time() - timenow


# Mode to idle
def going_to_idle():
    pedestrian_lights.red.on()
    sleep(1)
    car_lights.red.on()
    sleep(1)
    all_off()


def all_off():
    car_lights.red.off()
    car_lights.amber.off()
    car_lights.green.off()
    pedestrian_lights.red.off()
    pedestrian_lights.amber.off()
    pedestrian_lights.green.off()


# Mode iddle:
def idle_mode():
    timenow = time.time()
    timediff = 0
    while True:
        if pedestrian_button.is_pressed:
            print("Pedestrian button pressed!.")
            return 'no_idle'


        timediff = time.time() - timenow
        if timediff < 0.5:
            car_lights.amber.on()
            pedestrian_lights.red.off()
        elif timediff < 1.0:
            car_lights.amber.off()
            pedestrian_lights.red.on()
        else:
            timenow = time.time()


def main():
    mode = 'idle'
    while True:
         # check if pedestrian button is pressed
         mode = idle_mode()


         # traffic light mode
         if mode == 'idle':
             pass
         else:
             car_stop_mode()
             pedestrian_pass_normal_mode()
             pedestrian_pass_fast_mode()
             pedestrian_pass_ultrafast_mode()
             going_to_idle()
             mode = 'idle'


signal.signal(signal.SIGINT, handler)


main()
# Run the program indefinitely


pause()

