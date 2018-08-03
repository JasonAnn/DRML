import os

cuda_num = 3

class_number = 8
height = 200
width = 200
crop_height = 170
crop_width = 170

lr = 0.0001
lr_decay_every_epoch = 100
lr_decay_rate = 0.9

epoch = 1000
train_batch_size = 64
test_batch_size = 64
thresh = 0.8
test_every_epoch = 1



data_root = 'data/'
train_info = os.path.join(data_root, 'train_info.csv')
test_info = os.path.join(data_root, 'test_info.csv')

image_dir = os.path.join(data_root, 'face_images/')

