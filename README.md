# Home-OS
An example of a client / server application written in python 2.7 that can be used to automate electronics away from the server.
The source of the libraries imported for the hardware used in this program can be found here.
Pigpiod [python library]. (2014).
Retrieved from http://abyz.co.uk/rpi/pigpio/index.html
DHT-22 [python class]. (2014-07-11).
Retrieved from http://abyz.co.uk/rpi/pigpio/examples.html.

	Home OS, is an application written to bring home automation to anyone with a Raspberry Pi system on a chip. The client is to be installed on any system that is able to run python and C.  The Server is specifically meant to run on a Raspberry Pi system on a chip.  The Raspberry Pi should be fitted with a DHT-22 (Digital Humidity Temperature) sensor, as well as an LED light.  Aside from those specific components, an Ethernet connection, keyboard / pointer i/o and an hdmi screen connection are essential to getting the program up and running. I will begin with a description, discuss the main features, and give a summary of how the programs function.
	The raspberry pi system on a chip has 27 General Purpose Input Output pins (GPIO).  Raspberry Pi owners can use these pins to attach electronic devices and sensors to create many different useful projects.  Home OS assumes that a user has a DHT-22 on GPIO 17, and an LED light on GPIO 22.  The Home OS server side uses the pigpio library in conjunction with their class for the DHT-22 sensor from http://abyz.co.uk/rpi/pigpio/index.html, and the built in RPI.GPIO library to use the LED light, which is built into the raspberry pi python all I needed to do was import it.  The Home OS applications both rely on a TCP/IP socket to communicate with each other.  In addition to being connected via the socket, the client can then request a stream of temperature and humidity readings.  They can also signal to turn the LED on, or off.  The server also runs until the user exits the terminal, this program is meant to be left on all day, allowing the client to reconnect many times.
	The main features of the program are that the server will prime the sensors, prevent the electronics from locking, give the user control of the devices, and check user input to determine what action to take.  When first connecting the server automatically primes the sensors.  The DHT-22 needs to be primed, because the first two reads of temperature / humidity will return a value of -999.  So instead of printing this out and confusing the user, “Priming Sensors” is printed to the screen so the user knows what is going on.  After reading the value from the sensor twice, all is normal and works just fine.  So before the program prompts the user, it clears the junk data out of the sensor.  Wait timers are used because if the LED or sensor are triggered too fast they lock up, this is the reason I used a sleep timer between every decision the user enters.  By allowing the user to read the humidity and temperature, as well as turning the LED on and off, the user is given full control over these two devices.  Additionally the user input is checked so that if the user enters anything besides an identified command, it is interpreted as an exit command.
	The programs function first by having them both installed.  The Raspberry Pi must first run ‘sudo pigpiod’ in terminal to give the user root access to override the hardware security measures.  Next the raspberry pi runs ‘python server.py’ the client runs ‘python client.py’.  The Raspberry Pi is the device that should have the pigpio library and the dht-22 class installed as well as import the built in rpi.gpio library.  When the server is run, it will display ‘waiting for connection’, when the client is run it automatically connects.  There will be a confirmation in the server application and in the client application, ‘priming sensor…’ will be output each time the sensors are primed.  Then the client user will be given a menu.  Read the temperature / humidity with S, turn the LED on with O and off with F.  If the user reads the temperature / humidity, it will be streamed over the socket 6 times












