import socket
import threading
import thread
import time
import socketserver

l=[]
r=[]

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        print(cur_thread.name)
        l.append(self.request)
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        r.append(response)
        print(len(l))
        if len(l) == 3:
            for res in l:
                print(1)
#                res.sendall(response)
        #self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Client Received: {}".format(response))
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    thread.start_new_thread(client, (ip, port, "Hello World 1"))
    thread.start_new_thread(client, (ip, port, "Hello World 2"))
    thread.start_new_thread(client, (ip, port, "Hello World 3"))
    #client(ip, port, "Hello World 1")
    #client(ip, port, "Hello World 2")
    #client(ip, port, "Hello World 3")

    time.sleep(5)
    server.shutdown()
    server.server_close()
