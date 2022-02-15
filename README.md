

<div align="center">
  <img src="12321341234.PNG" alt="" width="25%" height="25%">
  <h1>恶评猎手</h1>
  <h4>基于多模型融合的恶意评论打分系统</h4>
</div>

本项目为2021年第一学期自然语言课程的课程设计项目。受Kaggle平台的[恶意评价竞赛](https://www.kaggle.com/c/jigsaw-toxic-severity-rating)的启发，通过融合基于Tf-Idf的机器学习模型与基于Bert的预训练模型构建了恶意评论打分系统。团队将此系统打包为可以直接使用的应用程序，并把将实现思路投稿至arXiv网站。

论文网址：[]()

### 项目架构

* `software`：编译好的程序文件
* `report_latex`:报告的latex源码
* `pic`：图片导出文件夹
* `input`：各大数据集
* `infer_model`:推理模型
* `code`：实现代码文件夹

### 模型训练与推理

模型的训练与推理在`code`文件夹下。

1. `Base_xxx.ipynb`表示的是基于机器学习的方案，`Bert_xxx`表示基于Bert预训练模型的方案。
2. `xxx_train.ipynb`表示训练代码，`xxx_infer`表示推理代码。
3. `EDA_xxx.ipynb`表示对不同训练集的开放数据探索。
4. `Display.ipynb`为项目展示代码

### 软件运行

程序运行的路径为`software\pack1\dist\infer1\infer1.exe`。直接运行```Toxic Comments Hunter```程序即可。需要调整一下窗口的大小以做到更好的呈现效果。输入一段恶意评论，或者是善意的评论，输出一个打分的分数。

![image-20211213131310691](https://gitee.com/AICollector/picgo/raw/master/img/image-20211213131310691.png)

### 关联项目

在此项目的基础上尝试了更多预处理模型，并参与Kaggle平台的[恶意评价竞赛](https://www.kaggle.com/c/jigsaw-toxic-severity-rating)。

项目地址：[]()



















