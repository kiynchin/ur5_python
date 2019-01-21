from multiprocessing import Process
from urscript import *

pLow = "-1.571,-2.01,-2.135,-0.563,1.571,0"
pMid = "-1.571,-1.571,-1.571,-1.571,1.571,0"
pHi = "-1.571,-1.615,-1.21,-1.883,1.571,0"
pLeft = "-1.971,-1.571,-1.571,-1.571,1.571,0"
pRight = "-1.171,-1.571,-1.571,-1.571,1.571,0"

def moveTo(pos,sock):
    urCommand("movel([{}],a=2, v=0.25, r=0.01)".format(pos),sock)


def trajectory1(sock):
    urCommand("def myProg():",sock)
    moveTo(pLow,sock)
    moveTo(pLeft,sock)
    moveTo(pHi,sock)
    moveTo(pRight,sock)
    moveTo(pMid,sock)
    urCommand("end",sock)
    

def trajectory2(sock):
    urCommand("def myProg():",sock)
    moveTo(pLow,sock)
    moveTo(pRight,sock)
    moveTo(pHi,sock)
    moveTo(pLeft,sock)
    moveTo(pMid,sock)
    urCommand("end",sock)


r.connect((RIGHT, PORT))
l.connect((LEFT,PORT))

procs = []
lProc = Process(target=trajectory1,args=(l,))
rProc = Process(target=trajectory2,args=(r,))
procs.append(rProc)
procs.append(lProc)

for proc in procs:
    proc.start()

for proc in procs:
    proc.join()

r.close()
l.close()
print("Program finish")


