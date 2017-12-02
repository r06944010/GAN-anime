import tensorflow as tf

directory = "*.py"
file_names = tf.train.match_filenames_once(directory)
queue = tf.train.string_input_producer(file_names, num_epochs=None, shuffle=True)

init = (tf.global_variables_initializer(), tf.local_variables_initializer())
# init = (tf.global_variables_initializer())

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(file_names))
