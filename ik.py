import socket
import time
import codecs
from urscript import *


r.connect((RIGHT, PORT))
time.sleep(0.05)
i = 0

while i<100:
	print(urCommand("get_inverse_kin(get_forward_kin())",r).decode("hex"))
	time.sleep(1)
	i+=1
r.close()
print("Program finish")


