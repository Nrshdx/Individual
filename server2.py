import socket
import threading
import os

def RetrieveFile(name, s):
    filename = s.recv(1024).decode()
    print (filename)
    if os.path.isfile(filename):
        exist = "Exist" + str(os.path.getsize(filename))
        s.send(str.encode(exist))
        response = s.recv(1024).decode()
        print(response)
        if response[:3] == 'yes':
            f = open(filename, 'rb')
            SendFile = f.read(1024)
            s.send(SendFile)
    else:
        message = "File Does Not Exist!!"
        s.send(message.encode())
    s.close()
    
def Main():
    host = "192.168.43.2"
    port = 8080
    
    s = socket.socket()
    s.bind((host,port))
    
    s.listen(5)
    
    print ("Server Started...")
    while True:
        conn, addr = s.accept()
        print ("Connection established from : " + str(addr))
        t = threading.Thread(target = RetrieveFile, args = ("retrivThread",conn))
        t.start()
    s.close()
    
Main()

