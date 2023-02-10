import urllib.request
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/EstrellaEspectro.txt'

filename = './Data/DatosMaximo.txt'

urllib.request.urlretrieve(url, filename)

data = np.loadtxt(filename)

plt.plot(data[:, 0], data[:, 1])
plt.savefig('./Data/EstrellaEspectro.png')