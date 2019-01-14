from multiprocessing import Process
from urscript import *

pLow = "-1.571,-2.01,-2.135,-0.563,1.571,0"
pMid = "-1.571,-1.571,-1.571,-1.571,1.571,0"
pHi = "-1.571,-1.615,-1.21,-1.883,1.571,0"
def trajectory(sock):
    urCommand("def myProg():",sock)
    urCommand("movel([{}],a=2, v=0.25, r=0.01)".format(pMid),sock)
    urCommand("movel([{}],a=2, v=0.25, r=0.01)".format(pHi),sock)
    urCommand("movel([{}],a=2, v=0.25, r=0.01)".format(pLow),sock)
    urCommand("end",sock)

r.connect((RIGHT, PORT))
l.connect((LEFT,PORT))

procs = []
lProc = Process(target=trajectory,args=(l,))
rProc = Process(target=trajectory,args=(r,))
procs.append(rProc)
procs.append(lProc)

for proc in procs:
    proc.start()

for proc in procs:
    proc.join()

r.close()
l.close()
print("Program finish")


