# Echo server program
import socket
import thread

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100)

clist = []

def connHandle(sock):
    data = conn.recv(1024)
    if len(clist) == 2:
        for lnk in clist:
            lnk.send(data)
    #print(data)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    clist.append(conn)
    thread.start_new_thread(connHandle, (conn,))
