#coding: utf8
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print('mnist end')
#将标签转换成one-hot矩阵
def dense_to_one_hot(labels_dense, num_classes=10):
  #ndarray.shape展示数组的维度，shape[0]展示行
  num_labels = labels_dense.shape[0]
  index_offset = np.arange(num_labels) * num_classes
  labels_one_hot = np.zeros((num_labels, num_classes))
  #numpy.darray.flat将数组变换成一维;numpy.ravel()返回视图
  labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
  return labels_one_hot

testFileName = 't10k-images.idx3-ubyte'
testLable = 't10k-labels.idx1-ubyte'
trainFileName = 'train-images.idx3-ubyte'
trainLable = 'train-labels.idx1-ubyte'

fileTrain = open(trainFileName, 'rb')
fileTrainLable = open(trainLable, 'rb')
buff = fileTrain.read()
TrainBuff = fileTrainLable.read()
fileTrain.close()
fileTrainLable.close()

fileTest = open(testFileName, 'rb')
fileTestLable = open(testLable, 'rb')
buffTest = fileTest.read()
BuffTestLable = fileTestLable.read()
fileTest.close()
fileTestLable.close()

dataTrain = np.frombuffer(buff[16:], dtype=np.uint8)
dataTrain = dataTrain.reshape(60000, 784)
TrainLabel = np.frombuffer(TrainBuff[8:], dtype=np.uint8)
TrainLabel = TrainLabel.reshape(60000, 1)
TrainLabel = dense_to_one_hot(TrainLabel)
#print('dataShape:',dataTrain.shape, 'data[0]:', dataTrain[0])

dataTest = np.frombuffer(buffTest[16:], dtype=np.uint8)
dataTest = dataTest.reshape(10000, 784)
TestLabel = np.frombuffer(BuffTestLable[8:], dtype=np.uint8)
TestLabel = TestLabel.reshape(10000, 1)
TestLabel = dense_to_one_hot(TestLabel)

x = tf.placeholder("float", [None, 784])
y_ = tf.placeholder("float", [None,10])

W1 = tf.Variable(tf.random_normal([784,300]))
b1 = tf.Variable(tf.random_normal([300]))
h1 = tf.nn.relu(tf.matmul(x,W1) + b1)
W2 = tf.Variable(tf.random_normal([300,10]))
b2 = tf.Variable(tf.random_normal([10]))

W1 = tf.Variable(tf.random_normal([784,10]))
b1 = tf.Variable(tf.random_normal([10]))
y = tf.nn.softmax(tf.matmul(x,W1) + b1)
'''
定义损失函数，y_是标签数据，乘以对应的计算出的y的log值，并全部求和，由于y是one-hot,故算出来的对数概率是
正确分类的对数概率和，取负值，求最小值
'''
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs = dataTrain[i*100%60000:i*100%60000+100]
  batch_ys = TrainLabel[i*100%60000:i*100%60000+100]
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: dataTest, y_: TestLabel}))