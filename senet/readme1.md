#SENet是早期Attention
核心思想是学习 feature Channel 间的关系，以凸显feature Channel 不同的重要度（也就是注意力分布），进而提高模型表现。

![alt picture](https://pic2.zhimg.com/v2-3ba4660b11053644db26aa6587016d99_r.jpg)

上图是SE Module 的示意图。给定一个输入 x，其特征通道数为 c_1，通过一系列卷积等一般变换后得到一个特徵通道数为 c_2 的特征。与传统的 CNN 不一样的是，接下来通过三个操作来重标定前面得到的特征。

首先是 Squeeze 操作，从空间维度来进行特征压缩，将h*w*c的特征变成一个1*1*c的特征，得到向量某种程度上具有全域性的感受野，并且输出的通道数和输入的特征通道数相匹配，它表示在特征通道上响应的全域性分布。公式非常简单，就是一个 global average pooling:
![alt gongshi](https://pic2.zhimg.com/v2-bae82e76f49627259ef0cd40fa90ada1_r.jpg)

其次是 Excitation 操作，通过引入 w 参数来为每个特征通道生成权重，其中引数 w 是可学习的，并通过一个 Sigmoid 的门获得 0~1 之间归一化的权重，完成显式地建模特征通道间的相关性。公式如下：
![alt gongshi](https://pic4.zhimg.com/v2-c1c19c8bed9fc6a30593e788b2980bd3_r.jpg)

最后是一个 Scale 的操作，将 Excitation 的输出的权重看做是经过选择后的每个特征通道的重要性，然后通过channel-wise multiplication 逐通道加权到先前的特征上，完成在通道维度上的对原始特征的重标定。公式如下：
![alt gongshi](https://pic1.zhimg.com/v2-a921553eef4fc05af13c2a3cc828d2ec_r.jpg)

![alt jiegou](https://pic1.zhimg.com/v2-be016e82174d230ec0b402c9dbbc8ecc_r.jpg)
虽然没有看到query、key和value的影子，但是其体现了不同channel应有不同权重，是早期的attention。

参考链接[zhihu](https://zhuanlan.zhihu.com/p/283125663)