#T2
import numpy as np
import matplotlib.pyplot as plt

def Henon_map (a, b, x0, y0, N):
    u = np.zeros((N+1, 2))
    u[0] = np.array([x0, y0])
    for i in range(N):
        u[i+1] = np.array([1 - a * u[i][0]**2 + u[i][1], b * u[i][0]])
    return u

#main:
a_range = 100

a = np.linspace(-a_range, a_range, 2 * a_range+1)

b = 0.3
x0, y0 = 0,0
N = 20

x = np.linspace(0, a_range, 2 * a_range+1)
for i in range(a_range):
    x[i] = Henon_map(a[i], b, x0, y0, N)[N, 0]
    # y[i] = Henon_map(a[i], b, x0, y0, N)[N-1, 1]

print(a)
print(x)

#下面是画图

plt.title('Henon map: arange = (-%d,%d), N = %d' % (a_range, a_range, N))

plt.plot(a, x, 'r-o')
plt.xlabel('a')
plt.ylabel('x')

# 显示网格
plt.grid(True)

plt.show()