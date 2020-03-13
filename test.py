import os
import numpy as np
import glob2

# 遍历文件夹中的txt文件
FilePaths = glob2.glob(r'toothdata\*.txt')  # 构造绝对路径，"\\"，其中一个'\'为转义符
print(FilePaths)
points = []

# 初始化数组下标
i = 0
for txtPath in FilePaths: # 遍历txt
    print(txtPath)
    point = []
    print(i)
    with open(txtPath) as f:  # 打开文件
        # 将txt文件中的数据存入数组
        while 1:
            line = f.readline()
            if not line:
                break
            strs = line.split(" ")
            point.append((float(strs[0]), float(strs[1]), float(strs[2]), float(strs[3]), float(strs[4]), float(strs[5])))
        # points原本为列表，需要转变为矩阵，方便处理
        point = np.array(point)
        points.append(point)
        point = []
    ++i
    print(points)
points = np.array(points)
print(points)
