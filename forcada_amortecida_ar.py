from numpy import sqrt
from scipy.optimize import curve_fit
from matplotlib import pyplot
import numpy as np
import pandas as pd


def objective(omega, f, m, b):
    w0 = 3.9
    gamma = b/m
    a = ((w0**2) - (omega**2))**2
    d = (4*(gamma**2)*(omega**2))
    return f/(m*sqrt(a+d))

file = pd.read_csv('frequencia_ar.csv', usecols= ['frequencia','amplitude'], sep=";")
x = list(float(a.replace(",", ".")) for a in list(file["frequencia"]))
y = list(float(b.replace(",", ".")) for b in list(file["amplitude"]))


popt, _ = curve_fit(objective, x, y)
f, m, b = popt


xdata = np.linspace(0,8,1000)
y__ = objective(xdata, f, m, b)
rng = np.random.default_rng()
y_noise = 0.2 * rng.normal(size=xdata.size)
ydata = y__ + y_noise
pyplot.plot(xdata, ydata, 'r-', label='data')

pyplot.xlabel("Frequência")
pyplot.ylabel("Amplitude")

pyplot.scatter(x, y)
pyplot.show()
