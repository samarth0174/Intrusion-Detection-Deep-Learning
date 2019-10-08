import socket
from time import sleep
import numpy as np

test_file = np.loadtxt("test1.txt")

#def main():
s = socket.socket()
s.connect(('127.0.0.1',4444))

print("Connected to Victim Server")

	

#index = 4 #normal
#index = 2 #dos
#index = 17 #Probe
#index = 13 #R2U

index = str(index).encode('utf-8')
s.send(index)
s.close()





#normal [0. 1. 0. 0. 0.] 4
#dos [1. 0. 0. 0. 0.] 2
#Probe  [0. 0. 1. 0. 0.] 17
#R2U [0. 0. 0. 1. 0.] 13
