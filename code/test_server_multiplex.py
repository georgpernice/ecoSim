import socket
import selectors #  im gleichen Prozess mehrere Sockets verwalten

# get server IP Address:
hostname = socket.gethostname()
serverIP = socket.gethostbyname(hostname)


# create a server with a non blocking socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 50000))
server.setblocking(False)
server.listen(1)



def accept(selector, sock):
    connection, addr = sock.accept()
    connection.setblocking(False)
    selector.register(connection, selectors.EVENT_READ, message)

def message(selector, client):
    nachricht = client.recv(1024)
    ip = client.getpeername()[0]
    if nachricht:
        print("[{}] {}".format(ip, nachricht.decode()))
    else:
        print("+++ Verbindung zu {} beendet".format(ip))
        selector.unregister(client)
        client.close()

# use this server in a selector, binding the READ event
# to the calback function "accept()"
selector = selectors.DefaultSelector()
selector.register(server, selectors.EVENT_READ, accept)

print("Starting up a multiplexing server \n"+serverIP+"\nwhich can serve to many clients.. ")
while True:
    for key, mask in selector.select():
        key.data(selector, key.fileobj)
