import socket
import time
from multiprocessing import Process
RIGHT = "10.10.11.38"    # The right arm
LEFT = "10.10.11.64" # the left arm
PORT = 30002              # The same port as used by the server
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def urCommand(string,sock=r):
	string += "\n"
	byteString = string.encode()
	print("Sending command: {}".format(string))
	sock.send(byteString)
	data = sock.recv(1024)
	return data


