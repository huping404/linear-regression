# coding:utf-8
import math
import numpy as py
import copy
from pylab import *
import matplotlib.pyplot as plt


def hy(x_sample, theta):
    # print x_sample
    # print theta
    # print zip(theta, x_sample)
    # hypothsis = theta0 + theta1 * x1 + theta2 * x2 .....
    temp = [t * x for t,x in zip(theta, x_sample)]
    # print temp
    result = sum(temp)
    # print result
    return result


# Loss function L(w,b)
def jtheta(x_set, y_set, theta):
    # print zip([x_set], [y_set])
    result = sum([pow(hy(x, theta) - y, 2) for (x,y) in zip([x_set], [y_set])])
    result = result / 2
    return result


x_train = []
y_train = []
# 输入X,Y
# nums = input("Input example numbers:")
# dim = input("Input example dimensions:")
#
# for i in range(0, nums):
#     x_temp = []
#     x_temp.append(1)
#     for j in range(0, dim):
#         x_value = input("%d x:" % (j + 1))
#         x_temp.append(x_value)
#     y_temp = input("%d y:" % (i + 1))
#     x_train.append(x_temp)
#     y_train.append(y_temp)

nums = 10 # 10个样本数据
dim = 2 # 没个样本两个feature x
x_train = [
    [1, 2],
    [2, 1],
    [2, 3],
    [3, 5],
    [1, 3],
    [4, 2],
    [7, 3],
    [4, 5],
    [11, 3],
    [8, 7]
]
y_train = [7, 8, 10, 14, 8, 13, 20, 16, 28, 26]

# print x_train
# print y_train

# PLOT EXAMPLE POINTS
if dim == 1:
    x_point = [item[1] for item in x_train]
    y_point = y_train
    plot(x_point, y_point, 'ro')
    axis([0, 6, 0, 6])

# 初始化所有参数theta为0
theta = [0 for i in range(dim)]
# print theta

# 初始化learning rate
rate = 0.0001

# learning begin
last_j = 0.0 # 最终最小偏差
current_j = 0.0  # 当前偏差
first_flag = True
k = 0
allTheta = []
while True:
    k = k + 1
    theta_last = theta

    for j in range(0, dim):
        # 求偏导
        sum_temp = sum([(y-hy(x, theta_last)) * x[j] for (x, y) in zip(x_train, y_train)])
        # 重新计算参数theta
        theta[j] = theta[j] + rate * sum_temp
        # print theta
        # print x,y
        current_j = jtheta(x, y, theta)
        print current_j

        if(first_flag == True):
            first_flag = False
        else:
            if current_j >= last_j:
                theta = theta_last
                print "found the minimum j(last one), break."
                print ""
                print "the hypothsis theta is :"
                print theta
                exit()

        last_j = current_j

        # t1 = arange(0.0, 6.0, 0.02)
        # plot(t1, theta[0] + theta[1] * t1, 'b')
        #
        # legend(('Samples', 'Hypo Lines'), loc='upper left')
        # title('LMS learning algorithm')
        # show()

