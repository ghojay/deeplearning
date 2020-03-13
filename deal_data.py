#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from read_data import drawcloud
from matplotlib import pyplot as plt


p=drawcloud()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []
a = []
b = []
w = []

# print(p.size)
for i in range(p.size//6):
    x.append(p[i][0])
    y.append(p[i][1])
    z.append(p[i][2])
    a.append(p[i][3])
    b.append(p[i][4])
    w.append(p[i][5])

# ax.scatter(x, y, z, a, b, w, c='k', marker='.', s=0.1)

ax.scatter(x, y, z,  c='k', marker='.', s=0.1)
ax.scatter(a, b, w,  c='k', marker='.', s=0.1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
