import gzip
import numpy as np


def extract_mnist_labels(raw_data_path: str, processed_data_path: str) -> None:
    """Extracts labels from raw MNIST labels data file and saves to np array

    Args:
        raw_data_path (str): path to raw MNIST labels data file
        processed_data_path (str): path to save np array containing labels 
    """
    with gzip.open(raw_data_path, 'rb') as f:
        f.seek(8)
        labels_bytes = f.read()
    labels_arr = np.array(list(labels_bytes), dtype=np.uint8).flatten()
    np.save(processed_data_path, labels_arr)
    
def extract_mnist_images(raw_data_path: str, processed_data_path: str) -> None:
    """Extracts images from raw MNIST image data file and saves to np array

    Args:
        raw_data_path (str): path to raw MNIST image data file
        processed_data_path (str): path to save np array containing (flattened) image arrays 
    """
    img_list = [] 
    with gzip.open(raw_data_path, 'rb') as f:
        f.seek(8)
        num_rows = int.from_bytes(bytes=f.read(4), byteorder='big', signed=False)
        num_cols = int.from_bytes(bytes=f.read(4), byteorder='big', signed=False)
        buffer_size = num_rows * num_cols
        while chunk := f.read(buffer_size):
            img_arr = np.array(list(chunk), dtype=np.uint8)
            img_list.append(img_arr)
        
    images_arr = np.array(img_list)
    np.save(processed_data_path, images_arr)
        
def process_mnist() -> None:
    """Process raw MNIST data into np arrays that are ready to be used for model training/testing
    """
    RAW_TRAIN_IMAGES_PATH = 'src/datasets/mnist/raw/train-images-idx3-ubyte.gz'
    RAW_TEST_IMAGES_PATH = 'src/datasets/mnist/raw/test-images-idx3-ubyte.gz'
    RAW_TRAIN_LABELS_PATH = 'src/datasets/mnist/raw/train-labels-idx1-ubyte.gz'
    RAW_TEST_LABELS_PATH = 'src/datasets/mnist/raw/test-labels-idx1-ubyte.gz'
    
    PROCESSED_TRAIN_IMAGES_PATH = 'src/datasets/mnist/processed/train-images.npy'
    PROCESSED_TEST_IMAGES_PATH = 'src/datasets/mnist/processed/test-images.npy'
    PROCESSED_TRAIN_LABELS_PATH = 'src/datasets/mnist/processed/train-labels.npy'
    PROCESSED_TEST_LABELS_PATH = 'src/datasets/mnist/processed/test-labels.npy'
    
    extract_mnist_images(RAW_TRAIN_IMAGES_PATH, PROCESSED_TRAIN_IMAGES_PATH)
    extract_mnist_images(RAW_TEST_IMAGES_PATH, PROCESSED_TEST_IMAGES_PATH)
    extract_mnist_labels(RAW_TRAIN_LABELS_PATH, PROCESSED_TRAIN_LABELS_PATH)
    extract_mnist_labels(RAW_TEST_LABELS_PATH, PROCESSED_TEST_LABELS_PATH)
