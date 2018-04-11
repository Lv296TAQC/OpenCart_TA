"""Singleton for driver"""

from selenium.webdriver import Chrome

# pylint: disable=too-few-public-methods
class Wrapper:
    """Wraper for driver"""
    instans = None
    conection = None

    def __new__(cls, *args, **kwargs):
        if not cls.instans:
            cls.instans = super(Wrapper, cls).__new__(cls, *args, **kwargs)
        return cls.instans

    def webdriver_rem(self):
        """Init driver"""
        self.conection = Chrome()
        return self.conection
