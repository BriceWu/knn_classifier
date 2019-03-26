#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from sklearn.datasets import make_blobs
# 导入KNN分类器
from sklearn.neighbors import KNeighborsClassifier
# 导入画图工具
import matplotlib.pyplot as plt
# 导入数据集拆分工具
from sklearn.model_selection import train_test_split


def generate_data():
    """
    生成样本数为200，分类为2的数据集
    :return:
    """
    data = make_blobs(n_samples=200, centers=2, random_state=8)
    X, y = data
    # 将生成的数据可视化
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.spring, edgecolors='k')
    plt.show()
    print 'over'


if __name__ == "__main__":
    generate_data()
