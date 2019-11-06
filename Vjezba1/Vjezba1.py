import socket
import time
import threading
import sys

received_msg=""
sending_msg=""
my_msg=""
condition = False

def start_server():
    global received_msg
    global sending_msg
    server=socket.socket()
    host=socket.gethostname()
    port=int(sys.argv[1])
    server.bind((host, port))
    server.listen(3)

    while True:
        c,addr=server.accept()
        received_msg=(c.recv(1024)).decode()
        c.close()


def connect_to_server():
    global my_msg
    global received_msg
    global sending_msg
    global condition
    try:
        host=socket.gethostname()
        port=int(sys.argv[2])
        
        while True:
            time.sleep(2)

            if (sending_msg!=received_msg and received_msg!=my_msg):
                print(received_msg)
                c = socket.socket() 
                c.connect((host, port))
                c.send(received_msg.encode())
                c.close()
                sending_msg=received_msg

            if (condition == True):
                c = socket.socket()
                c.connect((host, port))
                c.send(my_msg.encode())
                condition = False
                sending_msg = my_msg
                c.close()
    except Exception as e:
        connect_to_server()
        
def msg_input():
        while True:
            global my_msg
            my_msg = raw_input()
            global condition
            condition = True



threading._start_new_thread(start_server,())
threading._start_new_thread(msg_input,())
connect_to_server()
