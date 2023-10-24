# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:41:44 2023

@author: Brandon Sato
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as linalg
from scipy.optimize import curve_fit


#imports and reads data
data = pd.read_csv("signal.dat",delimiter = "|")
time = data["               time "]
signal = data["                signal "]
time.to_numpy()
signal.to_numpy()

#creates empty np array
fdata = np.zeros(shape=(1000,2))

#formats the data to np array
for x in range(1000):
    fdata[x][0]=time[x]
    fdata[x][1]=signal[x]
    
"""
A = np.column_stack([np.sin(fdata[:,0]) + np.cos(fdata[:,0]) + np.ones_like(fdata[:,0])])
(U,w,VT) = linalg.svd(A)

c = np.linalg.pinv(A).dot(fdata[:,1])

def polynomial_fit(coefficients, x):
    return np.polyval(coefficients, x)

x_fit = np.linspace(min(fdata[:,0]), max(fdata[:,0]), 1000)
y_fit = polynomial_fit(c, x_fit)

residuals = fdata[:,1]-y_fit
#plt.plot(fdata[:,0],residuals,'b.')

#plt.plot(time,signal,'r.')
#plt.plot(x_fit,y_fit,'b-')
#plt.ylabel("signal")
#plt.xlabel("time")

"""
t=fdata[:,0]
y=fdata[:,1]


# Function to fit a Fourier series
def fourier_series(t, a0, *coeffs):
    result = a0
    n = len(coeffs) // 2
    period = len(t) / 2  # Half the time span
    for i in range(n):
        result += coeffs[i] * np.cos(2 * np.pi * (i + 1) * t / period)
        result += coeffs[i + n] * np.sin(2 * np.pi * (i + 1) * t / period)
    return result

# Initial guesses for parameters (you may need to adjust these)
a0_guess = np.mean(y)
num_harmonics = 3  # Adjust the number of harmonics as needed
coeffs_guess = np.zeros(2 * num_harmonics)

# Fit the Fourier series to the data
popt, _ = curve_fit(fourier_series, t, y, p0=[a0_guess, *coeffs_guess])

# Generate the fitted curve
y_fit = fourier_series(t, *popt)

# Plot the original data and the fitted Fourier series
plt.plot(t, y, 'r.')
plt.plot(t, y_fit, 'b.')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
#print( np.max(w) / np.min(w))
