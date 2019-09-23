import serial
import threading
from time import sleep

PORT = "COM4"
BAUDS = 9600

serial_port = serial.Serial()

def read():
    while True:
        data = serial_port.read(9999)
        if len(data) > 0:
            print ("Got from Arduino: " + str(data))
        sleep(1)

def main():
    serial_port.baudrate = BAUDS
    serial_port.port = PORT
    serial_port.timeout = 0
    if serial_port.isOpen(): serial_port.close()
    serial_port.open()
    t1 = threading.Thread(target=read, args=())
    t1.start()
    while True:
        try:
            command = input('Enter a command to send to Arduino: \n\t')
            serial_port.write(str.encode(command))
        except KeyboardInterrupt:
            break
    serial_port.close()

main()