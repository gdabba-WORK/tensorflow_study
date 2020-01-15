# This Python file uses the following encoding: utf-8
import tensorflow as tf

# 상수 정의하기 --- (#1)

a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
v = tf.Variable(0, name="v")

calc_op = a + b + c
# assign_op = 