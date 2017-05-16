import socket

s = socket.socket()
host = socket.gethostname()
port = 5055
s.connect((host, port))
while True:
    pakets = s.recv(1024)
    if (pakets == '1'):
        break

    if (pakets == 'start'):
        decision = raw_input("Get Temperature (S)\nL.E.D \nOn (O) \nOff (F) \n(other to exit) \n Command : ")
        #print 'Decision is: ' + decision + '\n'
        s.send(decision)
        if ((decision != 'S') and (decision != 'O') and (decision != 'F')):
            print 'Closing...'
            break
        
    else:
        print (pakets)


s.close
