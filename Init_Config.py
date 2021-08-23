import serial , time
def open_connection(port):

    console= serial.Serial(port=port , baudrate=960, stopbits=1, bytesize=8)
    if console.isOpen():
        print("Serial Successfully connected!!")
        return console
    else:
        print("Fail")
        return 0

def read_from_console(console):

    numberOfBytes= console.inWaiting()
    print(numberOfBytes)

    if numberOfBytes:
        data=console.read(numberOfBytes)
        return data.decode()
    else:
        return False

def run_command(console , command='\n', sleep =3):
    console.write(command.encode()+b'\n')
    time.sleep(sleep)

def check_initDialog(console):
    run_command(console)
    output=read_from_console(console)

    if 'Would you like to enter the initial configuration dialog? [yes/no]:' in output:

        run_command(console,'no')
        run_command(console,'\n',15)
        run_command(console,'\r\n')
        return True
    else:
        return False

