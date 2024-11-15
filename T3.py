#T2
#为什么a>-23，x会恒等于0？
import numpy as np
import matplotlib.pyplot as plt

def Henon_map (a_in_f, b, x0, y0, N):
    u = np.zeros((N+1, 2))
    u[0] = np.array([x0, y0])
    for i in range(N):
        u[i+1] = np.array([1 - a_in_f * u[i][0]**2 + u[i][1], b * u[i][0]])
    return u

#main:
a_range = 50
points = 200

a = np.linspace(-a_range, a_range, points) 

b = 0.3
x0, y0 = 0,0
N = 100

x = np.zeros(points)
for i in range(points): ##这里有问题，不是a_range，而应该是points!!
    x[i] = Henon_map(a[i], b, x0, y0, N)[N, 0]

print(a)
print(x)


print('a =', a[np.argmin(np.abs(x))])
print('x =', x[np.argmin(np.abs(x))])

#下面是画图

plt.title('Henon map: arange = (-%d,%d), N = %d' % (a_range, a_range, N))

plt.plot(a, x, 'r-o')
plt.xlabel('a')
plt.ylabel('x')

# 显示网格
plt.grid(True)

plt.show()
