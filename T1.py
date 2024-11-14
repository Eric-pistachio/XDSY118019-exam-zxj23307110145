#hello
#题目分析：
#第一题是简单的迭代计算
#第二题“探索 N 的取值，求解得到的轨迹”什么意思？，加一个画图matplotlib
#第三题：作图
#第四题：找到Hénon map可以收敛到⼀条周期性轨道的 a 值，计算轨迹，绘图
#用到：matplotlib, numpy？, sympy？


#T1
import numpy as np
b = 0.3
a, x0, y0, N = list(map(int, input("Input a, b, x0, y0, N with a space.\n").split()))
u = np.zeros((N+1, 2))
u[0] = np.array([x0, y0])
print(u[0])
for i in range(N):
    u[i+1] = np.array([1 - a * u[i][0]**2 + u[i][1], b * u[i][0]])
    
print(u)