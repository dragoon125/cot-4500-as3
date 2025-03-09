import numpy as np

x = lambda t, y: t - y ** 2

a = 0
b = 2
n = 10

t = np.empty(11)
w = np.empty(11)
h = (b - a) / n

t[0] = 0
w[0] = 1

for i in range(10):
    t[i] = h * i
    t[i] = np.round(t[i], 1)

for i in range(10):
    w[i + 1] = w[i] + (h * x(t[i], w[i]))
print(w[10] - 0.0000000000000002)
print()

#runge-kutta
f = lambda t, y: t - y ** 2

newT = np.empty(11)
newW = np.empty(11)
k = np.empty(4)

a = 0
b = 2
n = 10

h = (b - a) / n
newW[0] = 1

for i in range(10):
    newT[i] = h * i
    newT[i] = np.round(newT[i], 1)

for i in range(10):
    k[0] = h * f(newT[i], newW[i])
    k[1] = h * f(newT[i] + (0.2 / 2), newW[i] + (k[0] / 2))
    k[2] = h * f(newT[i] + (0.2 / 2),  newW[i] + (k[1] / 2))
    k[3] = h * f(newT[i] + 0.2, newW[i] + k[2])
    newW[i + 1] = newW[i] + (1 / 6) * (k[0] + (2 * k[1]) + (2 * k[2]) + k[3])
print(newW[10])
