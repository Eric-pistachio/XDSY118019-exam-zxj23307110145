#T2
import numpy as np
import matplotlib.pyplot as plt

a_range = 2

a = np.linspace(0, a_range, a_range)

b = 0.3
x0, y0 = 0, 0
N = 3

u = np.zeros((a_range, N+1, 2))
for j in range(a_range):
    u[j, 0] = np.array([x0, y0])
print(u)

# for j in range(a_range):
#     for i in range(N):
#         u[j][i+1] = np.array([1 - a[j] * u[i][0]**2 + u[i][1], b * u[i][0]])

# x = np.linspace(0, a_range, a_range)
# x = u[N, 0]
# print(x)

# plt.plot(a, x, 'r-x')
# plt.xlabel('a')
# plt.ylabel('x')

# # 显示网格
# plt.grid(True)

# plt.show()