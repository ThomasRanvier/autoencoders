import tensorflow as tf
import tensorflow_datasets as tfds

def generic_processing(temp_ds, test_ds, info, batch_size, transforms):
    temp_ds = temp_ds.map(transforms, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    
    eval_ds = temp_ds.take(int(info.splits['train'].num_examples / 10.))
    train_ds = temp_ds.skip(int(info.splits['train'].num_examples / 10.))
    
    train_ds = train_ds.cache()
    train_ds = train_ds.shuffle(info.splits['train'].num_examples)
    train_ds = train_ds.batch(batch_size)
    train_ds = train_ds.prefetch(tf.data.experimental.AUTOTUNE)

    eval_ds = eval_ds.batch(batch_size)
    eval_ds = eval_ds.cache()
    eval_ds = eval_ds.prefetch(tf.data.experimental.AUTOTUNE)

    test_ds = test_ds.map(transforms, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    test_ds = test_ds.batch(batch_size)
    test_ds = test_ds.cache()
    test_ds = test_ds.prefetch(tf.data.experimental.AUTOTUNE)
    
    return (train_ds, eval_ds, test_ds)


def generic_processing_train_test_eval(train_ds, test_ds, eval_ds, info, batch_size, transforms):
    train_ds = train_ds.map(transforms, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    train_ds = train_ds.cache()
    train_ds = train_ds.shuffle(info.splits['train'].num_examples)
    train_ds = train_ds.batch(batch_size)
    train_ds = train_ds.prefetch(tf.data.experimental.AUTOTUNE)
    
    eval_ds = eval_ds.map(transforms, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    eval_ds = eval_ds.batch(batch_size)
    eval_ds = eval_ds.cache()
    eval_ds = eval_ds.prefetch(tf.data.experimental.AUTOTUNE)

    test_ds = test_ds.map(transforms, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    test_ds = test_ds.batch(batch_size)
    test_ds = test_ds.cache()
    test_ds = test_ds.prefetch(tf.data.experimental.AUTOTUNE)
    
    return (train_ds, eval_ds, test_ds)


def load_mnist(batch_size):
    (temp_ds, test_ds), info = tfds.load('mnist',
                                        split=['train', 'test'],
                                        shuffle_files=True,
                                        as_supervised=True,
                                        with_info=True,
                                        data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        return img, img
    
    return generic_processing(temp_ds, test_ds, info, batch_size, transforms)


def load_noisy_mnist(batch_size):
    (temp_ds, test_ds), info = tfds.load('mnist',
                                        split=['train', 'test'],
                                        shuffle_files=True,
                                        as_supervised=True,
                                        with_info=True,
                                        data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        noisy_img = img + .25 * tf.random.normal(shape=img.shape)
        noisy_img = tf.clip_by_value(noisy_img, clip_value_min=0., clip_value_max=1.)
        return noisy_img, img
    
    return generic_processing(temp_ds, test_ds, info, batch_size, transforms)


def load_fashion_mnist(batch_size):
    (temp_ds, test_ds), info = tfds.load('fashion_mnist',
                                        split=['train', 'test'],
                                        shuffle_files=True,
                                        as_supervised=True,
                                        with_info=True,
                                        data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        return img, img
    
    return generic_processing(temp_ds, test_ds, info, batch_size, transforms)


def load_noisy_fashion_mnist(batch_size):
    (temp_ds, test_ds), info = tfds.load('fashion_mnist',
                                        split=['train', 'test'],
                                        shuffle_files=True,
                                        as_supervised=True,
                                        with_info=True,
                                        data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        noisy_img = img + .25 * tf.random.normal(shape=img.shape)
        noisy_img = tf.clip_by_value(noisy_img, clip_value_min=0., clip_value_max=1.)
        return noisy_img, img
    
    return generic_processing(temp_ds, test_ds, info, batch_size, transforms)


def load_cifar(batch_size):
    (temp_ds, test_ds), info = tfds.load('cifar10',
                                        split=['train', 'test'],
                                        shuffle_files=True,
                                        as_supervised=True,
                                        with_info=True,
                                        data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        return img, img
    
    return generic_processing(temp_ds, test_ds, info, batch_size, transforms)


def load_noisy_cifar(batch_size):
    (temp_ds, test_ds), info = tfds.load('cifar10',
                                        split=['train', 'test'],
                                        shuffle_files=True,
                                        as_supervised=True,
                                        with_info=True,
                                        data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        noisy_img = img + .15 * tf.random.normal(shape=img.shape)
        noisy_img = tf.clip_by_value(noisy_img, clip_value_min=0., clip_value_max=1.)
        return noisy_img, img
    
    return generic_processing(temp_ds, test_ds, info, batch_size, transforms)


def load_celeb(batch_size):
    (train_ds, test_ds, eval_ds), info = tfds.load('celeb_a',
                                                    split=['train', 'test', 'validation'],
                                                    shuffle_files=True,
                                                    as_supervised=True,
                                                    with_info=True,
                                                    data_dir='D:\datasets')
    
    def transforms(image, label):
        img = tf.cast(image, tf.float32) / 255.
        return img, img
    
    return generic_processing_train_test_eval(train_ds, test_ds, eval_ds, info, batch_size, transforms)