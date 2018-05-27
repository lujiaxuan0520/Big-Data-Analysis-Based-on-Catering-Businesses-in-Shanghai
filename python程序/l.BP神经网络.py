#!/usr/bin/python
#coding=utf-8
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import scale
import xlrd

# neuron_size为输入神经元的列表，第一个元素为输入层元素的个数,最后一个为输出层元素
class Bpnn:
    def __init__(self, neuron_size, learning_rate):
        self.input_holder = tf.placeholder(tf.float32, [None, neuron_size[0]])
        self.output_holder = tf.placeholder(tf.float32, [None, neuron_size[-1]])
        self.weight = {}
        self.bias = {}
        self.layers = {}
        for i in range(len(neuron_size) - 1):
            #第i+1层神经元与前一层输入的各个权重w组成的矩阵
            self.weight[i+1] = tf.Variable(tf.random_normal([neuron_size[i], neuron_size[i+1]]))
        for i in range(len(neuron_size) - 1):
            #第i+1层每个神经元的偏移量b
            self.bias[i+1] = tf.Variable(tf.random_normal([neuron_size[i+1]]))
        #layers存放第i层wx+b作用relu激活函数后的结果
        self.layers[1] = tf.nn.relu(tf.add(tf.matmul(self.input_holder, self.weight[1]), self.bias[1]))
        layer_stack = [self.layers[1]]
        for i in range(len(neuron_size) - 1):
            if i != 0 and i != 1:
                #计算中间层的layers:r(wx+b)
                self.layers[i] = tf.nn.relu(tf.add(tf.matmul(layer_stack[-1], self.weight[i]), self.bias[i]))
                layer_stack.append(self.layers[i])
        #outlayer为预测的输出值
        self.out_layer = tf.add(tf.matmul(layer_stack[-1], self.weight[len(neuron_size) - 1]), self.bias[len(neuron_size) - 1])
        #损失函数：计算输出的目标值与预测值的偏差
        self.loss = tf.reduce_mean(tf.reduce_sum(tf.square(self.output_holder - self.out_layer), reduction_indices=[1]))
        self.train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(self.loss)
        self.init = tf.global_variables_initializer()
        self.sess = tf.Session()

    def train1(self, _input, _output):
        self.sess.run(self.init)
        for i in range(200000):
            self.sess.run(self.train_step, feed_dict={self.input_holder: _input, self.output_holder: _output})
            print(self.sess.run(self.loss, feed_dict={self.input_holder: _input, self.output_holder: _output}))
            print(self.sess.run(self.out_layer, feed_dict={self.input_holder: _input, self.output_holder: _output}))

    def predict(self, _input):
        f=open('predict_result.txt','w')
        for each_input in _input:
            each_input = each_input.reshape(1, len(each_input))
            f.write(str(self.sess.run(self.out_layer, feed_dict={self.input_holder: each_input})).lstrip('[ ').rstrip(']'))
            f.write('\n')
        f.close()

def readData():
    data = xlrd.open_workbook('训练集.xlsx')
    table = data.sheets()[0]
    input_arr = np.array([None, None, None, None, None, None, None, None, None])
    output_arr = np.array([None])
    for i in range(1, 50256):
        geoLat = table.cell(i, 6).value
        geoLng = table.cell(i, 7).value
        avgPrice = table.cell(i, 10).value
        shopPower = table.cell(i, 11).value
        popularity = table.cell(i, 13).value
        hasBookSetting = table.cell(i, 14).value
        hasShortDeals = table.cell(i, 15).value
        hasTakeAway = table.cell(i, 16).value
        branchTotal = table.cell(i, 17).value
        avg_score = table.cell(i, 12).value
        row = np.array(
            [geoLat, geoLng, avgPrice, shopPower, popularity, hasBookSetting, hasShortDeals, hasTakeAway, branchTotal])
        input_arr = np.row_stack((input_arr, row))
        output_arr = np.row_stack((output_arr, [avg_score]))
    input_arr = np.delete(input_arr, 0, 0)  # 删除第一行
    output_arr = np.delete(output_arr, 0, 0)
    np.save("input_arr.npy", input_arr)
    np.save("output_arr.npy", output_arr)

if __name__=='__main__':
    #训练数据
    input_arr=np.load("input_arr.npy")
    output_arr=np.load("output_arr.npy")
    #测试数据
    test_input_arr = np.loadtxt("测试集input_arr.txt")
    test_output_arr=np.loadtxt("测试集output_arr.txt")
    input_arr=scale(input_arr)
    test_input_arr=scale(test_input_arr)
    model=Bpnn([9,5,5,1],0.025)
    model.train1(input_arr,output_arr)
    model.predict(test_input_arr)

    #计算平均误差
    predict_result=np.loadtxt("predict_result.txt")
    test_output_arr = np.loadtxt("测试集output_arr.txt")
    avg_error=(np.abs(predict_result-test_output_arr))/test_output_arr
    avg_error=np.mean(avg_error)
    print('平均误差：',str(avg_error))

