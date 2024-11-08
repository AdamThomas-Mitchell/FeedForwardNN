import logging
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError, ContentTooShortError

def download_mnist():
    """Method to download MNIST raw data
    """
    TRAIN_IMAGES_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/train-images-idx3-ubyte.gz'
    TRAIN_LABELS_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/train-labels-idx1-ubyte.gz'
    TEST_IMAGES_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/t10k-images-idx3-ubyte.gz'
    TEST_LABELS_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/t10k-labels-idx1-ubyte.gz'
    MAX_ATTEMPTS = 3
    
    logging.info('Downloading MNIST raw data...')
    for retry_attempt in range(MAX_ATTEMPTS):
        try:
            # TODO: should I have a separate function for general urlretrive from given url?
            urlretrieve(TRAIN_IMAGES_ADDRESS, 'src/datasets/mnist/raw/train-images-idx3-ubyte.gz')
            urlretrieve(TRAIN_LABELS_ADDRESS, 'src/datasets/mnist/raw/train-labels-idx3-ubyte.gz')
            urlretrieve(TEST_IMAGES_ADDRESS, 'src/datasets/mnist/raw/test-images-idx3-ubyte.gz')
            urlretrieve(TEST_LABELS_ADDRESS, 'src/datasets/mnist/raw/test-labels-idx3-ubyte.gz')
            logging.info('MNIST raw data successfully downloaded to src/datasets/mnist/raw')
            break
        except HTTPError as ex:
            if retry_attempt < (MAX_ATTEMPTS - 1):
                logging.warning(f'HTTP error when attempting to download MNIST data: {ex.code} - {ex.reason}')
                logging.info('Retrying...')
            else:
                logging.error(f'Failed to download MNIST data - {ex.code} - {ex.reason}')
        except URLError as ex:
            if retry_attempt < (MAX_ATTEMPTS - 1):
                logging.warning(f'Failed to download MNIST data: {ex.reason}')
                logging.info('Retrying...')
            else:
                logging.error(f'Failed to download MNIST data: {ex.reason}')
        except ContentTooShortError:
            if retry_attempt < (MAX_ATTEMPTS - 1):
                logging.warning('Amount of downloaded data is less than the expected amount')
                logging.info('Retrying...')
            else:
                logging.warning('Amount of downloaded data is less than the expected amount - data may not be correct')        