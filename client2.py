import socket

def Main() :
    host = "192.168.43.2"
    port = 8080
    
    s = socket.socket()
    s.connect((host,port))
    
    print ("Connecting to server...")
    
    
    print ("Server Connected!")
    
    filename = input("File name? : ")
    if filename != 'x':
        s.send(str.encode(filename))
        filedata = s.recv(1024).decode()
        print (filedata)
        if filedata[:5] == "Exist":
            filesize = int(filedata[5:])
            message = input("File Exist, " + str(filesize)+"Bytes, do you want to download? (Y/N) : ")
            if message == 'y':
                response = "yes"
                s.send(str.encode(response))
                f = open('new_' + filename,'wb')
                filedata = s.recv(1024)
                tRecv = len(filedata)
                f.write(filedata)
        else:
            print ("File Does Not Exist!")
    
    s.close()


Main()
