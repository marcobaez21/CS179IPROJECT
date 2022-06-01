import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
# the ip address or hostname of the server, the receiver
host = "128.110.218.224"
# the port, let's use 5001
port = 8080
# the name of file we want to send, make sure it exists
filename = "porsche.jpg"
# get the file size
filesize = os.path.getsize(filename)
# create the client socket
s = socket.socket()
print("[+] Connecting to {}:{}".format(host, port))
s.connect((host, port))
print("[+] Connected.")
#bet='Hello Server'
#s.send(bet.encode())
# send the filename and filesize
s.send("{}{}{}".format(filename, SEPARATOR, filesize).encode())
# start sending the file
progress = tqdm.tqdm(range(filesize), "Sending file", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
 #       received = s.recv(BUFFER_SIZE).decode()
  #      print(data.decode())
# close the socket
#received = s.recv(BUFFER_SIZE).decode()
#while data:
 #   print(data.decode())

s.close()
