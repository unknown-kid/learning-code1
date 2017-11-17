import tensorflow as tf
import numpy as np
#定义变量两层的w
w_r = tf.Variable(tf.random_normal([2,5], stddev=2))
w_y = tf.Variable(tf.random_normal([5,1], stddev=2))
#定义常量两层的b
b_r = tf.Variable(tf.constant(2.0, shape=[5]))
b_y = tf.Variable(tf.constant(2.0, shape=[1]))
X=[[[1.0,2.0]],[[2.0,3.0]],[[3.0,4.0]],[[5.0,6.0]],[[7.0,8.0]]]
Y=[[[2.0]],[[6.0]],[[12.0]],[[30.0]],[[56.0]]]
#表示能够接收更新
x = tf.placeholder(tf.float32,shape=(1,2))
t = tf.placeholder(tf.float32,shape=(1,1))
#正向传播
b = tf.nn.tanh(tf.matmul(x,w_r)+b_r)
y = tf.nn.relu(tf.matmul(b,w_y)+b_y)
#s损失函数
loss = tf.reduce_mean(tf.square(t-y))
#梯度下降
train_step = tf.train.AdamOptimizer(0.01).minimize(loss)
#建立会话来运行TensorFlow
sess = tf.InteractiveSession()
#初始化所有变量的值
tf.global_variables_initializer().run()
#循环T次来进行训练
for i in range(10000):
         for j in range(5):
                  sess.run(train_step,feed_dict={x:X[j],t:Y[j]})
print(sess.run(w_r))
print(sess.run(b_r))
print(sess.run(y,feed_dict={x:[[1.0,3.0]]}))
sess.close()
