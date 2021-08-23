#################For Testing Serial Connection#######################

import serial
# with serial .Serial(port='COM5')as console:
#     if console.isOpen():
#         print("Serial Connected success!")
#     else:
#         print("Sorry")


##########################################################################

############For Testing the router Config$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# import serial ,time
# with serial.Serial(port='COM5') as console:
#     if console.isOpen():
#         print("Connected Success")
#         console.write(b'en\n')
#         time.sleep(1)
#         console.write(b'terminal length 0 \n')
#         time.sleep(1)
#         console.write(b'show ip int brief \n')
#         time.sleep(2)
#         numberofBytes= console.inWaiting()
#         data= console.read(numberofBytes)
#         print(data.decode())
#     else:
#         print("Sorry you can't connect")


############For initial COnfig####################
import Init_Config as init

mycon= init.open_connection('COM1')


if mycon:
    # init.check_initDialog(mycon)
    # init.run_command(mycon)
    with open('config.txt','r+') as file:
        for cmd in file:
            init.run_command(mycon,cmd)
output= init.read_from_console(mycon)
print(output)