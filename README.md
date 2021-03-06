# Python_Learning_DEMO
存储个人在Python学习过程中用到的一些样例demo，以便在以后的学习以及工作中用来调用和参考。
## Machine_Learning/DL/demo/
### day_04.py
该py模块下主要是关于Tensorflow中的一些基本操作，包括图和会话、张量和基本运算以及变量和模型的保存加载。同时，主要以自实现一个线性回归预测为例，讲解了tensorflow中的这些基本操作的使用方法。下面
给出学习过程中的一些重点笔记：  
  
*1.Tensor中形状的概念*  
形状分为静态形状和动态形状。对于静态形状来说，一旦张量形状固定了呃，不能再次设置静态形状，并且不能跨纬度修改，只能1D->1D，2D->2D等。对于动态形状来说，可以去
创建一个新的张量，改变时候一定要注意元素数量匹配，可进行跨纬度修改，如1D->2D，1D->3D等。 
  
*2.变量的创建*  
```Python  
tf.Variable(initial_value=None,name=None,trainable=True)  
```  
创建一个带有值initial_value的新变量，其中trainable参数为True时指定定义的这个变量能跟着梯度下降一起优化。**在使用Tensorflow编程时，模型参数必须使用变量定义，否则无法
训练模型。**与普通张量op相比，变量op能够持久化保存。同时在定义一个变量op时，一定要在会话中进行初始化。  
```Python  
 var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0), name="variable")  
 # 必须做一步显示的初始化op  
 init_op = tf.global_variables_initializer()  
 with tf.Session() as sess:  
     # 必须运行初始化op  
     sess.run(init_op)  
     print(sess.run(var))
```  
*3.模型的保存和恢复*  
*4.自定义命令行参数*  
*5.可视化tensorboard的一些操作*  
  
### day_05.py  
该py模块下，是关于tensorflow中的线程队列和IO操作的一些demo，包括：模拟同步数据的处理、模拟异步子线程、csv文件的读取、图片文件的读取
、二进制文件的读取以及tensorflow自带的文件格式TFRcord文件的使用。  
**NT:** TFRecord是一种二进制文件，写入内容为Example协议快，该协议块是一种类字典的格式。  
  
### day_06.py  
该py模块下，主要是关于实现单层(全连接层)实现手写数字识别以及卷积神经网络识别手写数字的demo。
  
1.感知机模型  
感知机是用来解决分类问题的。有n个输入数据，通过权重与各数据之间的计算和，比较激励函数结果，
得到输出(设定阈值来进行分类)。**应用:** 很容易解决与、或问题。  
  
2.人工神经网络(ANN)  
基础神经网络：单层感知器，线性神经网络，BP神经网络，Hopfield神经网络等  
进阶神经网络：玻尔兹曼机，受限玻尔兹曼机，递归神经网络等  
深度神经网络：深度置信网络，卷积神经网络，循环神经网络，LSTM网络等   
  
3.卷积神经网络

