import logging

import configparser

from datetime import datetime



import constants as c





class Config(object):

	"""docstring for Config"""



	_instance = None

	log_level = logging.ERROR



	def __new__(cls, *args, **kwargs):

		if cls._instance is None:

			cls._instance = object.__new__(cls, *args, **kwargs)



			cls._instance.app_name = 'aloha-ip-checker'



			cls._instance.config = configparser.ConfigParser()



			try:

				cls._instance.config.read_file(open(c.CONF_FILE))



				app_params = cls._instance.config['app']



				if 'name' in app_params:

					cls._instance.app_name = app_params['name']



				if 'log_level' in app_params:

					cls._instance.log_level = logging.getLevelName(app_params['log_level'])



				if 'mode' in app_params:

					cls._instance.mode = app_params['mode']



			except Exception as e:

				print(f'Config Error: {e}')



		return cls._instance





class Logger(Config):

	"""docstring for Logger"""



	_instance = None



	def __new__(cls, *args, **kwargs):

		if cls._instance is None:

			cls._instance = super().__new__(cls, *args, **kwargs)

			cls._instance._initialized = False



			# Creating an object

			cls._instance._logger = logging.getLogger(cls._instance.app_name)



			# Setting the threshold of logger

			cls._instance._logger.setLevel(cls._instance.log_level)



			# create console handler and set level to debug

			ch = logging.StreamHandler()

			ch.setLevel(cls._instance.log_level)



			# create formatter

			formatter = logging.Formatter('%(asctime)s - %(levelname)7s - %(message)s', datefmt='%y%m%d %I:%M:%S')



			# # add formatter to ch

			ch.setFormatter(formatter)



			# add ch to logger

			cls._instance._logger.addHandler(ch)



			cls._instance._logger.info(f'App: {cls._instance.app_name}, Log level: {logging.getLevelName(cls._instance.log_level)}')



		return cls._instance



	@staticmethod

	def get_logger():

		return Logger()._logger





class TimeParser(object):

	"""docstring for TimeParser"""



	def __init__(self):

		super(TimeParser, self).__init__()

		self.logger = Logger.get_logger()

		self.TIME_FORMAT = c.TIME_FORMAT



	def parse(self, time_arg):



		self.logger.debug(f'Parse command line arguments')

		self.logger.debug(f'Arg: {time_arg}')



		times = [x.strip() for x in time_arg.split(',')]



		self.logger.debug(f'Total {len(times)} time samples discovered')



		unique_times = {}



		for t in times:

			try:

				v_time = datetime.strptime(t, self.TIME_FORMAT)

			except ValueError as e:

				self.logger.warn(f'Invalid time {t}')

				pass

			else:

				key = str(v_time.time())

				unique_times[key] = 1 + unique_times[key] if key in unique_times else 1



		self.logger.info(f'Total {len(unique_times.keys())} unique time slots discovered (out of {len(times)})')



		return unique_times