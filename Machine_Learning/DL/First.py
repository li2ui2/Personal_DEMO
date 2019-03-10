import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 去除警告

# 创建一张图,包含一组op和tensor，上下文环境
# op：只要使用tensorflow的API定义的函数都是op
# tensor：就指代的是数据

g = tf.Graph()
with g.as_default():
    c = tf.constant(11.0)
    print(c.graph)


# 实现一个加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)
sum1 = tf.add(a, b)

# 默认的这张图，相当于是给程序分配一段内存
graph = tf.get_default_graph()
# print(graph)

# 不是op不能运行
var1 = 1.0
# var2 = 2.0
# sum2 = var1 + var2

# 有重载的机制,默认会给运算符重载成op类型
sum2 = a + var1
print(sum2)

# 只能运行一个图，可以在会话当中指定图去运行
# 添加config=tf.ConfigProto(log_device_placement=True)，可以显示tensor命名等信息
# with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
# 只要有会话的上下文环境，就可以使用eval()函数

# 训练模型
# 实时的提供数据去进行训练
# placeholder是一个占位符,feed_dict是一个字典
plt = tf.placeholder(tf.float32, [None, 3])  # ?X3形状的数据

with tf.Session() as sess:
    print(sess.run(sum2))
    print(sess.run(plt, feed_dict={plt: [[1, 2, 3], [2, 3, 4]]}))
    # print(sum1.eval())
    # 查看元素在哪一张图中
    # print(a.graph)
    # print(sum1.graph)
    # print(sess.graph)
