# 期末考Part1 README

解答代码合成为一个finalexampart1.ipynb文件
## 问题描述及解答思路
### 问题1
- 输⼊任意函数系数 a, b 、初始值 u0(x0, y0) 以及轨迹⻓度 N；
- 根据下面公式迭代计算出ui，代码中用u[i]表示

$$x_{n+1}=1-ax_n^2+y_n$$
$$y_{n+1} = bx_n$$
- 按顺序输出u[i]
### 问题2
- 取经典Hénon map的轨迹的参数取值： a=1.4, b=0.3, u0=(0, 0) 
- 改变N求轨迹，并以x 为横坐标， y 为纵坐标绘制轨迹图
### 问题3
- 固定 b=0.3 ，取a为一系列的点（利用numpy library中的linespace函数）后获得⼀系列Hénon map的轨迹
- 以 a 为横轴， x 为纵轴绘制orbit digram图
### 问题4
- 分析上述orbit digram，找到Hénon map可以收敛到⼀条周期性轨道的 a 值
- 计算这时的轨迹并以x 为横坐标， y 为纵坐标绘制轨迹图

## 代码使用方法
具体见ipynb文件中的提示