import numpy as np
from scipy.spatial import distance
# a = (1, 2, 3);  b = (4, 5, 6)
# print(distance.euclidean(a, b))
## 測試點的座標 = (tx, ty)   
y0 = 0
x1 = -9.7
y1 = 4.74
x2 = -4.5
y2 = 7.79
x3 = 19
y3 = -18

# def triposition(x, y)
# 原點 = 第10點 (0,0)
ori = np.array((0,0))
## 第一定位點 loc1 到原點距離 = (x1, y1)
loc1 = np.array((x1, y1))
d1 =  np.linalg.norm(loc1 - ori)
print('r1 =', d1)

## 第二定位點 loc2 到原點距離 = (x2, y2)
loc2 = np.array((x2, y2))
d2 = np.linalg.norm(loc2 - ori)
print('r2 =',d2)

## 第三定位點 loc3 到原點距離 = (x3, y3)
loc3 = np.array((x3, y3))
d3 = np.linalg.norm(loc3 - ori)
print('r3 =',d3)

# AX = b 
bx = (x1**2 + y1**2 -d1**2) - (x3**2 + y3**2 - d3**2) 
by = (x2**2 + y2**2 -d2**2) - (x3**2 + y3**2 - d3**2) 

A = np.array([[2*(x1 - x3), 2*(y1 - y3)], 
              [2*(x2 - x3), 2*(y2 - y3)]])
print('A =',A)

b = np.array([[bx], 
              [by]])
print('b =',b)

X = np.linalg.lstsq(A,b, rcond=0)[0]
print('X =',X)

x_ls = np.linalg.inv(A.transpose() * np.mat(A)) * A.transpose() * b
print('x_ls=', x_ls)
