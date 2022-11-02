import time,utime
from machine import Pin
from RotaryEncoder import Rotary
from SevSeg import RunnerV8

rotary = Rotary(34, 35, 32) # Register and init rotary encoder
display = RunnerV8() # Init display
val = 100 # Start at random velocity


""""
    4 pasos hacen una vuelta
"""
def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        if val > 10:
            val = (val - 10)
        print(val)
    elif change == Rotary.ROT_CCW:
        if val < 500:
            val = (val + 10)

rotary.add_handler(rotary_changed)

def sendStepToStepper(paso, tipo, bobinas):
    bit = 1
    for i in range(4):
        if (tipo[paso]  & bit) == 0:
            bobinas[i].off()
        else:
            bobinas[i].on()
        bit = bit << 1

def main():
    global val


    #Define los pines del Motor PaP
    motor_pins = (13, 12, 11, 10)

    #Configura las GPIO como Salidas
    bobinas = list()
    for i in motor_pins:
        bobinas.append( Pin(i, Pin.OUT) )

    #Secuencia a 1 paso
    un_paso  = ( int('1000',2),
                int('0100',2),
                int('0010',2),
                int('0001',2) )

    sentido = True
    configuracion = 1
    contador_pasos = 0
    cantidad_pasos = 3

    while True:
        if sentido:
            contador_pasos += 1
            if contador_pasos > cantidad_pasos:
                contador_pasos = 0
        else:
            contador_pasos -= 1
            if contador_pasos < 0:
                contador_pasos = cantidad_pasos

        if configuracion == 1:
            sendStepToStepper(contador_pasos, un_paso, bobinas)
            cantidad_pasos = 3

        display.send_data({100/val})
        while val == 500:
            pass
        utime.sleep_ms(val)

if __name__ == '__main__':
    main()
