



<div align="center">
  <img src="https://gitee.com/AICollector/picgo/raw/master/12321341234.PNG" alt="" width="25%" height="25%">
  <h1>恶评猎手</h1>
  <h4>基于多模型融合的恶意评论打分系统</h4>

### 项目架构：

* software：编译好的程序文件
* report_latex:报告的latex源码
* refer：一些自己写的博客以及参考的文章
* pic：报告用到的一些图片
* input：各大数据集
* infer_model:最终推理的模型
* code：实现代码文件



**项目体验**

1. 本地运行程序：直接运行```Toxic Comments Hunter```程序即可。需要调整一下窗口的大小以做到更好的呈现效果。输入一段恶意评论，或者是善意的评论，输出一个打分的分数。

![image-20211213131310691](https://gitee.com/AICollector/picgo/raw/master/img/image-20211213131310691.png)





**文件架构**

* software：编译好的程序文件
* report_latex:报告的latex源码
* refer：一些自己写的博客以及参考的文章
* pic：报告用到的一些图片
* input：各大数据集
* infer_model:最终推理的模型
* code：实现代码文件



**代码复现**

所有的代码均可以复现。其中EDA打头的文件是数据探索文件。Base打头的是机器学习模型。Bert打头的是Bert预训练模型。由于文件量太大，模型就没有放到文件下。其中机器学习模型我们的训练的模型如下：

![image-20211213141629870](https://gitee.com/AICollector/picgo/raw/master/img/image-20211213141629870.png)

实验的记过在record下可以看到。Bert模型我们在本地环境下无法配置，我们在Kaggle的服务器上进行了实验，下面是实验内容。

![image-20211213100943142](https://s2.loli.net/2021/12/13/3TSBVF17ItRAMia.png)















