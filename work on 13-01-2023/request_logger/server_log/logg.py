import requests, logging
from datetime import datetime


class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
            print(cls._instance)
            cls._instance._app_name = 'harshit'

            cls._instance._format = '%(asctime)s  %(message)s'

            cls._instance._level = logging.getLevelName('DEBUG')

            cls._instance._filepath = 'E:\Aloha Assisment\work on 13-01-2023\logs\mylog3.log'

        return cls._instance


class Logger(Config):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

            cls._instance._logger = logging.getLogger(cls._instance._app_name)

            cls._instance._logger.setLevel(cls._instance._level)

            logging.basicConfig(filename=cls._instance._filepath, format=cls._instance._format)

        return cls._instance

    @staticmethod
    def get_logger():
        return Logger()._logger


class Request(object):

    def __init__(self, app_name):
        self.logger = Logger.get_logger()

        self.logger.info('Logging configuration Done by using singleton patten')


if __name__ == '__main__':
    r = Request('harshit')
