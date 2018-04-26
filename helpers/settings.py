"""
Module contains settings.
"""
import logging

import os

BASE_HOST = "http://localhost/opencart"
PHONES = {
    "IPHONE": "iPhone",
    "HTC": "HTC Touch HD",
    "PALM": "Palm Treo Pro"
}
BASE_USER_EMAIL = "taqc296@gmail.com"
BASE_USER_PASSWORD = "root"
BASE_CONNECTION = "mysql://root@localhost/opencart"
URL = "http://127.0.0.1/index.php?route=product/product&product_id=47"

PRESET_BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "dbpresets"))
DB_PRESET = {
    "user_base": os.path.join(PRESET_BASE_PATH, "user", "base.sql"),
    "guest_base": os.path.join(PRESET_BASE_PATH, "guest", "base.sql")
}

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
