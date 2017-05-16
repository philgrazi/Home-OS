import pigpio
import RPi.GPIO as GPIO
import DHT22
import socket
from time import sleep
# 'sudo pigpiod' in terminal
#bypass security to access hardware
#socket object
s = socket.socket()
#socket setup
host = socket.gethostname()
port = 5055
s.bind((host, port))
#led setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #debugging
GPIO.setup(22, GPIO.OUT)
#dht22 setup
#initiate gpio for pigpio
pi = pigpio.pi()
#setup sensor
dht22 = DHT22.sensor(pi, 17)
dht22.trigger()
#sleep more than 2 otherwise sensor data is garbage
sleepTime = 3
#function for reading and converting temp/humid signal
def readDHT22():
    #new reading
    dht22.trigger()
    #save val
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return (humidity, temp)


while True:
    print 'waiting for connection'
    s.listen(5)
    c, addr = s.accept()
    print 'connection from ', addr
    #clear the junk data    
    c.send('Welcome to home os \n')
    sensorPrimer = 0
    while (sensorPrimer < 2):
        c.send('Priming Sensor... \n')
        humidity, temperature = readDHT22()
        sleep(sleepTime)
        sensorPrimer = sensorPrimer + 1

    runs = 0
    while (runs < 10) :
        test = True
        c.send('start')
        choice = c.recv(1024)
        choice = str(choice)
        print 'Choice was ' + choice + '\n'
        if (choice == 'S'):
            test = False
            x = 0
            runs = runs + 1
            while (x < 6):
                humidity, temperature = readDHT22()
                c.send('Temperature is: ' + str(temperature) + 'c  ' + 'Humidity: ' + str(humidity) + '%')
                #c.send('Humidity is: ' + str(humidity))
                print 'Sent Temperature: ', temperature, 'Humidity: ',humidity
                sleep(sleepTime)
                x = x + 1
            
        elif (choice == 'O'):
            test = False
            GPIO.output(22,GPIO.LOW)
            sleep(sleepTime)
            runs = runs + 1
        elif (choice == 'F'):
            test = False
            GPIO.output(22,GPIO.HIGH)
            sleep(sleepTime)
            runs = runs + 1
        elif ((choice != 'S') and (choice != 'O') and (choice != 'F')):
            c.close()
            print 'session closed'
            break
        
        #elif (test == True):
         #   c.send('Session closing... \n')
          #  c.close()
           # print 'Session Terminating \n'
            #s.close()
            #break
        #pickup above this, cant terminate with controlability
        #examine notes big star

    

