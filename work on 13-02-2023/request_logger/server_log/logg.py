import requests, logging
from datetime import datetime


class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)

            cls._instance._app_name = 'harshit'

            cls._instance._format = logging.Formatter('%(asctime)s  %(message)s', datefmt='%d-%m-%Y %H:%M:%M')

            cls._instance._level = logging.getLevelName('DEBUG')

            cls._instance._filepath = 'E:\Aloha Assisment\work on 13-02-2023\logs\mylog2.log'

        return cls._instance


class Logger(Config):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

            cls._instance._logger = logging.getLogger(cls._instance.app_name)

            cls._instance._logger.setLevel(cls._instance.level)

            logging.basicConfig(filename=cls._instance.filepath)

        return cls._instance

    @staticmethod
    def get_logger():
        return Logger()._logger


class Request(object):

    def __init__(self, app_name):
        self.logger = Logger.get_logger()

        self.logger.info('hello')


if __name__ == '__main__':
    r = Request('harshit')

# need help for creating a variable creation and performing the same operation like sample.py file
