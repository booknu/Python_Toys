### 일반 python
x = 1
y = x + 9
print(y)

### TensorFlow 선언 영역
import tensorflow as tf

x = tf.constant(1, name = 'x')
y = tf.Variable(x + 9, name = 'y')
print(y)

print(y.value())

# 내가 사용한 Variable 타입들을 기본적인 값으로 초기화해줌
model = tf.global_variables_initializer()

### TensorFlow 실행 영역
# with를 사용하면 close를 안 해줘도 됨
with tf.Session() as sess:
    sess.run(model)
    print(sess.run(y))
