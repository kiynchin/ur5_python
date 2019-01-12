import socket
import time
RIGHT = "10.10.11.38"    # The right arm
LEFT = "10.10.11.64" # the left arm
PORT = 30002              # The same port as used by the server
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
length = 3
def urCommand(sock,string):
	string += "\n"
	byteString = string.encode()
	print("Sending command: {}".format(string))
	sock.send(byteString)

r.connect((RIGHT, PORT))
time.sleep(0.05)
urCommand(r,"movel([-1.571,-1.571,-1.571,-1.571,1.571,0],a=30, v=15, t={}, r=0)".format(length))
time.sleep(length)
urCommand(r,"movel([-1.571,-1.615,-1.21,-1.883,1.571,0],a=20.1, v=15, t={}, r=0)".format(length))
time.sleep(length)
urCommand(r,"movel([-1.571,-2.01,-2.135,-0.563,1.571,0],a=30, v=15, t={}, r=0)".format(length))
time.sleep(length)



r.close()
print("Program finish")


