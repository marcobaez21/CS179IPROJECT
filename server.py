import socket
import tqdm
import os
import pyffe
from pyffe.models import mAlexNet
import caffe
import numpy as np
from scipy.misc import imresize
# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print("[*] Listening as {}:{}".format(SERVER_HOST, SERVER_PORT))
client_socket, address = s.accept()
# if below code is executed, that means the sender is connected
print("[+] {} is connected.".format(address))
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), "Receiving file", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
#msg='Thank You!'
#client_socket.send(msg.encode())
input_format = pyffe.InputFormat(
    new_width=256,
    new_height=256,
    crop_size=224,
    scale=1. / 256,
    mirror=True
)
caffe.set_mode_cpu()
net = caffe.Net("mAlexNet-on-PKLot_train-val-PKLot_val/deploy.prototxt", "mAlexNet-on-PKLot_train-val-PKLot_val/snapshot_iter_6318.caffemodel", caffe.TEST)
img = caffe.io.load_image(filename)
img = imresize(img, [224, 224])
img = img.astype(np.uint8)
imageData = np.asarray([img.transpose(2, 1, 0)])
imageData = np.divide(imageData, 255.0)
out = net.forward_all(data=imageData)
print("Predicted class is #{}.".format(out))
# close the client socket
client_socket.close()
# close the server socket
s.close()
host = '128.110.218.214'
port=8080
s=socket.socket()
s.connect((host,port))
s.send(msg.encode())
s.close()
