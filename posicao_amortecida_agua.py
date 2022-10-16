from matplotlib import pyplot
import numpy as np
import pandas as pd
from numpy import cos
from numpy import exp

def objective(t, amp, gamma, w):
    return  amp * exp(gamma*t*(-1)) * cos(t*w) 

def error(params):
    amp, gamma, w = params
    model_func = objective(x, amp, gamma, w)
    z = y - model_func
    return z

file = pd.read_csv('data/posicao_agua_6.csv', usecols= ['tempo','espaco'], sep=";")

x = list(float(a) for a in list(file["tempo"]))
y = list(float(b) for b in list(file["espaco"]))

x = x - np.min(x)

xdata = np.arange(min(x), max(x), 0.1)
print(xdata)
metade = int(len(x)/2)

amp = y[0] - np.mean(y)
omega = np.pi*2/(x[2]-x[0])
gamma = np.log(abs(y[metade]/(amp*cos(omega*x[metade]))))/x[metade]
ydata = objective(xdata, amp, gamma, omega) 

y = y - np.mean(y)
# ydata = objective(xdata, *popt)
pyplot.plot(xdata, ydata, 'r-', label='data')

pyplot.xlabel("Tempo (s)")
pyplot.ylabel("Espaço (cm)")

pyplot.scatter(x, y)
pyplot.show()
