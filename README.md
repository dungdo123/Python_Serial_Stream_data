# Python_Serial_Data
 
 
- This code is used to read serial data from BME280 sensor in realtime including temperature, humidity and pressure
- Users can use USB cable, Bluetooth module(HC-05, HC-06) to communicate
- On linux system, this code could be change a little bit, you need permission to read data from serial port
command: sudo chmod 666 /dev/*name of device
- Setup bluetooth module on linux system:
   1. pair devices, password: 1234
   2. hcitool scan # to check MAC of bluetooth module
   3. setup rfcomm manually:
         sudo rfcomm bind 0 mac_address 1
   4. run code to read data
   5. release devices when finished:
        sudo rfcomm release rfcomm0

