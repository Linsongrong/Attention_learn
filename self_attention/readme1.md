## self_attention
Self-attention（NLP中往往称为Scaled-Dot Attention）的结构有三个分支：query、key和value。计算时通常分为三步：

![alt picture](https://pic4.zhimg.com/v2-00fc48ffa5e4a9025e2864a01c91b587_r.jpg)

第一步是将query和每个key进行相似度计算得到权重，常用的相似度函数有点积，cos相似度，拼接，感知机等；
![alt picture](https://pic1.zhimg.com/v2-4d04bd76bd02f07f3f8671609a498870_r.jpg)

第二步一般是使用一个softmax函数对这些权重进行归一化；

第三步将权重和相应的键值value进行加权求和得到最后的attention。

假设输入的feature maps的大小Batch_size×Channels×Width×Height，那么通过三个1×1卷积（分别是query_conv ， key_conv 和 value_conv）就可以得到query、key和value：

query：在query_conv卷积中，输入为B×C×W×H，输出为B×C/8×W×H；
key：在key_conv卷积中，输入为B×C×W×H，输出为B×C/8×W×H；
value：在value_conv卷积中，输入为B×C×W×H，输出为B×C×W×H。


参考链接[zhihu](https://zhuanlan.zhihu.com/p/283125663)