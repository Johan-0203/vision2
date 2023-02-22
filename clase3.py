import numpy as np
import matplotlib.pyplot as plt
import math

LR = 0.00002
EPOCHS = 20

dt = np.loadtxt('train.csv', delimiter=";")
x = dt[:,0,None]
y = dt[:,1,None]

#Estandarizar
x = (x-np.mean(x))/np.std(x)
y = (y-np.mean(y))/np.std(y)

plt.plot(x,y,"o")
# Columna de 1 a X
m = x.shape[0]
x_0 = np.ones((m,1))
x = np.hstack((x_0,x))

#Primeros valores del parametro
theta = np.random.rand(2)

print(theta[0],theta[1])

for i in range(EPOCHS):
    #Predecidos
    y_pred = x @ theta
    err = y_pred - y[0]
    errx= (y_pred-y[0]) * x[:,1]
    
    #Derivadas parciales
    dpar0 = np.sum(err)
    dpar1 = np.sum(errx)

    theta[0] -= LR * dpar0
    theta[1] -= LR * dpar1

    plt.plot(x[:,1], y_pred)

print(theta[0],theta[1])
plt.xlabel('Area',color='b')
plt.ylabel('Precio',color='g')
plt.title('Casas - Precio vs Area',color='r')
plt.show()


