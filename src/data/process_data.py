import gzip
import numpy as np
import matplotlib.pyplot as plt 

TEST_IMAGES_PATH = 'src/datasets/mnist/raw/test-images-idx3-ubyte.gz'
TEST_LABELS_PATH = 'src/datasets/mnist/raw/test-labels-idx3-ubyte.gz'
IMAGE_SIZE = 28

with gzip.open(TEST_IMAGES_PATH, 'rb') as f:
    magic_number = int.from_bytes(f.read(4), 'big')
    sample_count = int.from_bytes(f.read(4), 'big')
    print(magic_number)
    print(sample_count)
    # f.read(16)
    # buffer = f.read(IMAGE_SIZE * IMAGE_SIZE)
    # data = np.frombuffer(buffer, dtype=np.uint8).astype(np.uint32)
    # data = data.reshape(1, IMAGE_SIZE, IMAGE_SIZE, 1)
    
    # print(data)
    # print(data.shape)
    # print(data[0])
    # print(data[0].shape)
    # print(data[0].squeeze())
    # print(data[0].squeeze().shape)
    # plt.imshow(data[0].squeeze())
    # plt.show()