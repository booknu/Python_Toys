import tensorflow as tf

a = tf.constant(10, name = "a")
b = tf.constant(90, name = "b")

y = tf.Variable(a + b * 2, name = "y")

model = tf.global_variables_initializer()

# 이걸 실행하면 해당 위치에 파일이 쓰임
# 그 후 tensorboard 명령을 통해 그래프를 볼 수 있음
# 
with tf.Session() as sess:
    merged = tf.summary.merge_all() #
    writer = tf.summary.FileWriter("d:/temp/tensorflowlogs", sess.graph) # 파일의 위치(특정 위치)로 write
    sess.run(model)
    print(sess.run(y))


