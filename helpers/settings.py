"""
Module contains setings.
"""
import logging

BASE_HOST = "http://localhost/opencart"
BASE_USER_EMAIL = "taqc296@gmail.com"
BASE_USER_PASSWORD = "root"
BASE_CONNECTION = "mysql://root@localhost/opencart"

logging.basicConfig(filename="sample.log",
                    filemode='w',
                    format=('# %(levelname)-8s [%(asctime)s] '
                            '%(filename)-20s [LINE:%(lineno)s]   %(message)s'),
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
