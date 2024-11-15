#T1
import numpy as np
a = 0.2512562814070307
b = 0.3
x0, y0, N = list(map(int, input("Input a, b, x0, y0, N with a space.\n").split()))
u = np.zeros((N+1, 2))
u[0] = np.array([x0, y0])
print(u[0])
for i in range(N):
    u[i+1] = np.array([1 - a * u[i][0]**2 + u[i][1], b * u[i][0]])
    
print(u)