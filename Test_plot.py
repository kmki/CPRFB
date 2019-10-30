import numpy as np #Built array
import os # it is used to clean
#os.sytem('cls')#para windows
import matplotlib.pyplot as plt
from scipy import signal
from scipy import optimize

'''
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
a=plt.show()

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
b=plt.show()

# define true model parameters
x=np.linspace(-1, 1, 100)
a, b, c = 1, 2, 3
y_exact = a + b * x + c * x**2

 # simulate noisy data
m = 100
X = 1 - 2 * np.random.rand(m)
Y = a + b * X + c * X**2 + np.random.randn(m)

 # fit the data to the model using linear least square
A = np.vstack([X**0, X**1, X**2]) # see np.vander for alternative
sol, r, rank, sv = la.lstsq(A.T, Y)

y_fit = sol[0] + sol[1] * x + sol[2] * x**2
fig, ax = plt.subplots(figsize=(12, 4))

ax.plot(X, Y, 'go', alpha=0.5, label='Simulated data')
ax.plot(x, y_exact, 'k', lw=2, label='True value $y = 1 + 2x + 3x^2$')
ax.plot(x, y_fit, 'b', lw=2, label='Least square fit')
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$y$", fontsize=18)
ax.legend(loc=2)

'''
#def main()
    #open a file for writting and create it if id does not exist
f=open('t1_0', 'r')
f.close()
print(f)