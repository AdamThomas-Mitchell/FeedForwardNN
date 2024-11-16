import logging
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError, ContentTooShortError


def download_from_url(url: str, file_path: str, max_attempts: int = 3) -> None:
    """Download file from url and save to specified location

    Args:
        url (str): URL of file to be downloaded
        file_path (str): path to where the downloaded file is saved
        max_attempts (int, optional): maximum number of times to retry the URL download if issues occur. Defaults to 3.
    """
    logging.info(f'Downloading file from {url} and saving to {file_path}...')
    for retry_attempt in range(max_attempts):
        try:
            urlretrieve(url, file_path)
            logging.info('File successfully downloaded')
            break
        except HTTPError as ex:
            if retry_attempt < (max_attempts - 1):
                logging.warning(f'HTTP error when attempting to download file from {url}: {ex.code} - {ex.reason}')
                logging.info('Retrying...')
            else:
                logging.error(f'Failed to download file from {url}: {ex.code} - {ex.reason}')
        except URLError as ex:
            if retry_attempt < (max_attempts - 1):
                logging.warning(f'Failed to download file from {url}: {ex.reason}')
                logging.info('Retrying...')
            else:
                logging.error(f'Failed to download file from {url}: {ex.reason}')
        except ContentTooShortError:
            if retry_attempt < (max_attempts - 1):
                logging.warning(f'Amount of downloaded data from {url} is less than the expected amount')
                logging.info('Retrying...')
            else:
                logging.warning(f'Amount of downloaded data from {url} is less than the expected amount - data may not be correct')

def download_mnist() -> None:
    """Download the 4 raw data files for the MNIST dataset - train images, train labels, test images, test labels
    """
    TRAIN_IMAGES_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/train-images-idx3-ubyte.gz'
    TRAIN_LABELS_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/train-labels-idx1-ubyte.gz'
    TEST_IMAGES_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/t10k-images-idx3-ubyte.gz'
    TEST_LABELS_ADDRESS = 'https://storage.googleapis.com/cvdf-datasets/mnist/t10k-labels-idx1-ubyte.gz'
    
    logging.info('Downloading MNIST raw data...')
    download_from_url(TRAIN_IMAGES_ADDRESS, 'src/datasets/mnist/raw/train-images-idx3-ubyte.gz')
    download_from_url(TRAIN_LABELS_ADDRESS, 'src/datasets/mnist/raw/train-labels-idx1-ubyte.gz')
    download_from_url(TEST_IMAGES_ADDRESS, 'src/datasets/mnist/raw/test-images-idx3-ubyte.gz')
    download_from_url(TEST_LABELS_ADDRESS, 'src/datasets/mnist/raw/test-labels-idx1-ubyte.gz')       