# chat_client.py

import sys
import socket
import select
 
def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # below code is to connect to Remote Host
    try :
        s.connect((host, port))
    except :
        print 'Problem While Connecting'
        sys.exit()
     
    print 'Successfully Connected to remote host. Please start sending messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print '\nUser Disconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())