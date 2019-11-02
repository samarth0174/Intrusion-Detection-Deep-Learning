import socket
from tensorflow.keras.models import load_model
import numpy as np

test_file = np.loadtxt("testing.txt")
model1  = load_model('model1.h5')

s = socket.socket()
s.bind(('127.0.0.1',4444))
s.listen(1)

print("Binding & Listening is done")	
print("Waiting for accept")
print("Server established successfully")	

conn, addr = s.accept()

result = conn.recv(4048)
index = int(result.decode('utf-8'))

data = test_file[index].reshape(1,78)

pred1  = model1.predict(data)
y_classes = pred1.argmax(axis=-1)
# print(y_classes)
if(y_classes==0):
    print("DOS ATTACK DETECTED")
elif(y_classes==1):
    print("NORMAL PACKET DATA")
elif(y_classes==2):
    print("PROBE ATTACK(Probe) DETECTED")
elif(y_classes==3):
    print("REMOTE TO USER ATTACK(R2U) DETECTED")
        


print("Connection Close")
conn.close()


#normal [0. 1. 0. 0. 0.] 4
#dos [1. 0. 0. 0. 0.] 2
#Probe  [0. 0. 1. 0. 0.] 17
#R2U [0. 0. 0. 1. 0.] 13
