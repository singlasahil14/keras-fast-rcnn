import scipy.io
import numpy as np

mat = scipy.io.loadmat('data/selective_search_data/voc_2007_train.mat')
print(mat.keys())

images = np.squeeze(mat['images'])
images = images.tolist()
boxes = np.squeeze(mat['boxes'])
boxes = boxes.tolist()

im2boxes = {}
for img, img_boxes in zip(images, boxes):
    im2boxes[str(img[0])] = img_boxes.tolist()
print(im2boxes)
