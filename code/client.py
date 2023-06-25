import socket
# ip adresse speichern..
ip = input("IP-Adresse: ")

# socket als schnittstelle von programm zum internet initialisieren:
# AF_INET means IPv4 protocol , SOCK_STREAM -> use TCP Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connects to the socket with stored ip and port 50000
s.connect((ip, 50000))

print("starting up client..")
# start client behaviour
try: 
    while True: 
        nachricht = input("Nachricht: ")
        s.send(nachricht.encode()) 
        antwort = s.recv(1024) # buffersize 1024
        print("[{}] {}".format(ip, antwort.decode())) 
finally: 
    s.close()
