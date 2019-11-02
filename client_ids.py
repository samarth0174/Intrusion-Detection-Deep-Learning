import socket
from time import sleep
import numpy as np

test_file = np.loadtxt("testing.txt")

#def main():
s = socket.socket()
s.connect(('127.0.0.1',4444))

print("Connected to Victim Server")

	

index = 1 #normal
#index = 4 #dos
#index = 836 #Probe
#index =  3#R2U

index = str(index).encode('utf-8')
s.send(index)
s.close()





#normal [0. 1. 0. 0. 0.] 1
#dos [1. 0. 0. 0. 0.] 4
#Probe  [0. 0. 1. 0. 0.] 836
#R2U [0. 0. 0. 1. 0.] 3
