# This Python file uses the following encoding: utf-8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 상수 정의
a = tf.constant(1234)
b = tf.constant(5000)

# 계산 정의
add_op = a + b

