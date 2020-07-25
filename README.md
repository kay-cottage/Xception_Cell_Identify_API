# Xception_Cell4_Stable_For_amd64

A program with Xception which can identify a variety of cells


基于Xception深度可分离卷积神经网络训练的细胞形态识别软件

目前能够比较准确识别（测试集准确率大于90%）嗜酸性粒细胞，嗜碱性粒细胞，中性粒细胞，与成熟红细胞4种！


或者嗜酸性粒细胞，嗜碱性粒细胞，中性粒细胞，成熟红细胞，淋巴细胞，单核细胞与浆细胞7种！（后三者为差别更小的细粒度图像识别，由于数据非常有限，准确率有待提高!)



目前由于训练集数据非常有限，识别种类有待增多，欢迎大家前来改进模型，提供更多数据！


为个人想法的简单实现，旨在让更多人方便地用上AI细胞识别技术辅助诊断。


*注意：禁止用于商业用途，欢迎个人学习交流！*







**使用**

1.请先从以下链接下载我已训练好的Xception神经网络模型，（4种细胞识别）


链接：https://pan.baidu.com/s/1hdLoYS51IqcdVhB01w2yDw 提取码：X1z9



2.检查文件夹classes.txt文件中是否有需要识别细胞的类别名称（英文），即RBC，eosinophi，basophil，neutrophil


3.启动程序Xception_Cell4_Stable_For_amd64.exe,先点击model_path选择模型文件，点击识别，选择需要识别地细胞图像（尽量出现一个细胞）即可等待文本框返回结果！


**补充**


4种细胞识别神经网络模型（准确率更高）

下载链接：https://pan.baidu.com/s/1hdLoYS51IqcdVhB01w2yDw 提取码：X1z9


7种细胞识别神经网络模型

下载链接链接：https://pan.baidu.com/s/1xY5C5x9iDkS-dr2QGtcGng 提取码：X1z9


注意：本程序已经打包部分tensorflow环境，初次加载模型启动需要一段时间（10s或更长），退出需要重新加载模型，请耐心等待！


更多效果视频欢迎关注bilibili主页：https://space.bilibili.com/362186371


Github主页：https://github.com/kay-cottage




最后，不喜勿喷，谢谢！
