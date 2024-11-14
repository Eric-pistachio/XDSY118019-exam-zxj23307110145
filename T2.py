#T2
import numpy as np
import matplotlib.pyplot as plt

a = 1.4
b = 0.3
x0, y0 = 0, 0
N = int(input("Input N.\n"))

u = np.zeros((N+1, 2))
u[0] = np.array([x0, y0])
print(u[0])
for i in range(N):
    u[i+1] = np.array([1 - a * u[i][0]**2 + u[i][1], b * u[i][0]])

x = u[:, 0]
y = u[:, 1]
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