# coding:utf-8

import numpy as np

rate = 0.001
x_train = np.array([
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
])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test = np.array([[1, 4],[2, 2],[2, 5],[5, 3],[1, 5],[4, 1]])

# y = theta0 + theta1 * x1 + theta2 * x2

theta = [np.random.normal(), np.random.normal(), np.random.normal()]
last_l = 0
iter = 0
max_iter = 100

# 训练
while True:
    iter += 1
    current_l = 0
    diff = [0, 0, 0] # 偏微分

    for x, y in zip(x_train, y_train):
        y_f = theta[0] + theta[1] * x[0] + theta[2] * x[1]
        y_l = pow((y - y_f),2)
        current_l = current_l + y_l
        diff[0] += 2 * (y - y_f) * -1
        diff[1] += 2 * (y - y_f) * -x[0]
        diff[2] += 2 * (y - y_f) * -x[1]

    # if iter > max_iter:
    if((current_l >= last_l and last_l != 0)):
        break
    else:
        last_l = current_l

        # 梯度下降求新的theta
        theta[0] = theta[0] - rate * diff[0]
        theta[1] = theta[1] - rate * diff[1]
        theta[2] = theta[2] - rate * diff[2]
        # print theta

print theta,iter

# 测试
outcome = [int(theta[0]+theta[1]*x[0]+theta[1]*x[1]) for x in x_test]
print outcome



