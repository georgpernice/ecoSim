import socket

# user print context & obtain IPv4 address
print("Starting multiplex client. Enter your desired connection.. ")
ip = input("IP-Adresse: ")

# initialize a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50000))
try:
    while True:
        nachricht = input("Nachricht: ")
        s.send(nachricht.encode())
finally:
    s.close()
