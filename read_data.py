import os
import numpy as np
import glob2

#txts = ','.join(txts)#转化为非数组类型
#print (txts)

def drawcloud():
    FilePaths = glob2.glob(r'E:\研究生\毕业论文\toothdata\*.txt')  # 构造绝对路径，"\\"，其中一个'\'为转义符
    print(FilePaths)
    for txtPath in FilePaths:
        with open(txtPath) as f:  # 打开文件
            points = []
            while 1:
                line = f.readline()
                if not line:
                    break
                strs = line.split(" ")
                points.append((float(strs[0]), float(strs[1]), float(strs[2]), float(strs[3]), float(strs[4]), float(strs[5])))

            # points原本为列表，需要转变为矩阵，方便处理
        points = np.array(points)
    print(points)
    return points