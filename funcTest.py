import socket
import time
from urscript import *

r.connect((RIGHT, PORT))
length = 3
time.sleep(0.05)
urCommand("def myProg():")
urCommand("movel([-1.571,-1.571,-1.571,-1.571,1.571,0],a=2, v=0.25, r=0.01)")
urCommand("movel([-1.571,-1.615,-1.21,-1.883,1.571,0],a=2, v=0.25, r=0.01)")
urCommand("movel([-1.571,-2.01,-2.135,-0.563,1.571,0],a=2, v=0.25, r=0.01)")
urCommand("end")
time.sleep(length)



r.close()
print("Program finish")


