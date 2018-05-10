import time
import serial
check=1
# configure the serrial port S0 with the baudarte
port= serial.Serial(port='/dev/ttyS0',baudrate =9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

def gsm_init():
    # to check the modem put basic AT command
    port.write('AT'+'\r\n')
    #provide delay of 200ms to read data from GSM Module
    time.sleep(0.2)
    #Read 100 bytes from GSM Module
    print(port.read(100))
    #Attach or Detach from GPRS Service (Result  1 = Attach , 2 = Detached )
    port.write('AT+CGATT?'+'\r\n')
   
    time.sleep(0.2)
    #Read 100 bytes from GSM Module
    print(port.read(100))
    #start task and setting the APN
    port.write("AT+CSTT=\"airtelgprs.com\","","""+'\r\n')
    time.sleep(0.2)
    #Read 100 bytes from GSM Module
    print(port.read(100))
    #bring up wireless connection
    port.write("AT+CIICR"+'\r\n')
    #provide delay of 200ms to read data from GSM Module
    time.sleep(0.2)
    #Read 100 bytes from GSM Module
    print(port.read(100))
    #get local IP adress
    port.write("AT+CIFSR"+'\r\n')
    time.sleep(0.2)
    print(port.read(100))
    # Start TCP connection
    port.write("AT+CIPSPRT=0"+'\r\n')
    time.sleep(0.2)
    print(port.read(100))
    #start up the connection with particualr IP address and port number
    port.write("AT+CIPSTART=\"TCP\",\"XXXXXXXX Write your server IP address XXXXXXXXXX\",\"xxxxx Port Number xxxxxxxxx\""+'\r\n')
    time.sleep(0.5)
    print(port.read(100))
    
def Send_data_server():
    #sending data to Server 
    port.write(chr(26)+'\r\n')
    #Waitting for reply form server 
    time.sleep(0.5)
    a=(port.read(100))
    print a
    #port1.write(a)

def close_coonection():
    #Terminate Socket connection drom server
    port.write("AT+CIPCLOSE"+"\r\n")
    time.sleep(2)
    print(port.read(100))
    #Shut down the module
    port.write("AT+CIPSHUT"+"\r\n")
    time.sleep(2)
    print(port.read(100))

while True:
    try:
        if(check==1):
            close_coonection()
            gsm_init()
            check=0
        Send_data_server()
    except:
        print("Wait! for data sending")
   
