import tensorflow as tf

s = tf.constant(483)
v = tf.constant([1.1, 2.2, 3.3])
m = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t = tf.constant([[[2], [4], [6]], [[8], [10], [12]], [[14], [16], [18]]])

# 0은 blank로 나오지만, 어떤 값이든 될 수 있는건 None으로 표시됨
# ex) (None, 28,28)
print(s.shape)
print(v.shape)
print(m.shape)
print(t.shape)