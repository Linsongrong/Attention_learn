# -*- coding: UTF-8 -*-
'''
@Project ：Attention_learn 
@File    ：vot.py
@IDE     ：PyCharm 
@Author  ：linsongrong
@Date    ：2021/8/26 11:09 
'''
import os
os.environ["KMP_DUPLICATE_LIB_OK"]  =  "TRUE"

import torch
from d2l import torch as d2l

"""
为了可视化注意力权重，我们定义了 show_heatmaps 函数。
其输入 matrices 的形状是 (要显示的行数，要显示的列数, 查询的数目, 键的数目)。
"""
def show_heatmaps(matrices, xlabel, ylabel, titles=None, figsize=(2.5, 2.5), cmap='Reds'):
    d2l.use_svg_display()
    num_rows, num_cols = matrices.shape[0], matrices.shape[1]
    fig, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize,
                                 sharex=True, sharey=True, squeeze=False)
    for i, (row_axes, row_matrices) in enumerate(zip(axes, matrices)):
        for j, (ax, matrix) in enumerate(zip(row_axes, row_matrices)):
            pcm = ax.imshow(matrix.detach().numpy(), cmap=cmap)
            if i == num_rows - 1:
                ax.set_xlabel(xlabel)
            if j == 0:
                ax.set_ylabel(ylabel)
            if titles:
                ax.set_title(titles[j])
    fig.colorbar(pcm, ax=axes, shrink=0.6)
    fig.show()


if __name__ == '__main__':
    attention_weights = torch.eye(10).reshape((1, 1, 10, 10))
    show_heatmaps(attention_weights, xlabel='Keys', ylabel='Queries')