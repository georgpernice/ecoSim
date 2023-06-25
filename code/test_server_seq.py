import socket

#initialisiere ein socket als schnittstelle von programm zum internet über OS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to all server ip adresses and port 50000
s.bind(("", 50000)) 
s.listen(1)

print("Starting up server ...")
# enter the loop of event recognition
try: 
    while True: 
        komm, addr = s.accept()
        # komm.recv ein leerer String zurückgegeben  bedeutet 
        # Verbindungspartner hat die Verbindung beendet
        while True:
            # store received msg
            data = komm.recv(1024) 
            if not data: # client will send empty messag once onnection breaks
                print("Die Verbindung wurde vom Client unterbrochen!")
                komm.close()
                break
            print("[{}] {}".format(addr[0], data.decode())) 
            nachricht = input("Antwort: ")
            komm.send(nachricht.encode()) 
finally: 
    s.close()
