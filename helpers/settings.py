"""
Module contains setings.
"""
import logging

BASE_HOST = "http://localhost/opencart"
PRODUCT = "iPhone"
BASE_USER_EMAIL = "taqc296@gmail.com"
BASE_USER_PASSWORD = "root"
BASE_CONNECTION = "mysql://root@localhost/opencart"
URL = "http://127.0.0.1/index.php?route=product/product&product_id=47"

logging.basicConfig(filename="sample.log",
                    filemode='w',
                    format=('# %(levelname)-8s [%(asctime)s] '
                            '%(filename)-20s [LINE:%(lineno)s]   %(message)s'),
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
try:
    from .local_settings import *
except ImportError:
    pass
