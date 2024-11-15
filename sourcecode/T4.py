#T2
import numpy as np
import matplotlib.pyplot as plt

def Henon_map (a_in_f, b, x0, y0, N):
    u = np.zeros((N+1, 2))
    u[0] = np.array([x0, y0])
    for i in range(N):
        u[i+1] = np.array([1 - a_in_f * u[i][0]**2 + u[i][1], b * u[i][0]])
    return u

#main:
a = 0.7537688442210992
b = 0.3
x0, y0 = 0,0
N = int(input("Input N.\n"))

x = Henon_map(a, b, x0, y0, N)[:, 0]
y = Henon_map(a, b, x0, y0, N)[:, 1]

print(x)
print(y)

plt.plot(x, y, 'r-o')
# 添加标题和标签
plt.title('N = %d' % N)
plt.xlabel('x axis')
plt.ylabel('y axis')

# 显示图例
# plt.legend([''])

# 显示网格
plt.grid(True)

plt.show()