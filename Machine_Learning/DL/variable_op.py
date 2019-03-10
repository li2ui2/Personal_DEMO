import tensorflow as tf


# 变量op
# 1.变量op能够持久化保存，普通张量op是不行的
# 2.当定义一个变量op的时候，一定要在会话当中去运行初始化
# 3.name参数：在tensorboard使用的时候显示名字，可以让相同op名字的进行区分
a = tf.constant([1, 2, 3, 4, 5])

var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0))

print(a, var)

# 必须做一步显示的初始化op
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    # 必须运行初始化op
    sess.run(init_op)

    # 把程序的图结构写入时间文件
    file_writer = tf.summary.FileWriter("F:\\Workspace\\PycharmProject\\Machine_Learning\\DL\\summary\\test", graph=sess.graph)

    print(sess.run([a, var]))
