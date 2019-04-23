import numpy as np
import matplotlib.pylab as plt

def cos(x):
	return np.cos(x)

def sen(x):
	return -np.sin(x)

x=np.linspace(-100,100,1000)

plt.figure()
fig,ax=plt.subplots(2,1,figsize=(10,10))
ax[0].plot(x,cos(x),c='purple')
ax[1].plot(x,sen(x),c='black')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[0].set_title('Funcion $cos(x)$')
ax[1].set_title('Funcion derivada $-sin(x)$')
plt.savefig('GarzonCamilo_cosysin.pdf')
plt.close()
