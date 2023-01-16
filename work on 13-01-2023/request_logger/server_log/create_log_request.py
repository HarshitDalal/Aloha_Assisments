import requests, logging
from datetime import datetime
import json


class Logger:

    def __init__(self, name):
        self._app_name = name
        self.filepath = 'E:\Aloha Assisment\work on 13-01-2023\logs\mylog2.log'
        self.__formate = '%(asctime)s  %(message)s'

        logging.basicConfig(format=self.__formate, level=logging.DEBUG,
                            handlers=[
                                logging.FileHandler(self.filepath),
                                logging.StreamHandler()
                            ])

        self._config = logging.getLogger(self._app_name)

        self._config.warning(f'Statring log for {self._app_name} \n' + '-' * 130)
        self.__start_time = datetime.now()

    def __del__(self):
        end_time = datetime.now()
        diff = end_time - self.__start_time
        self._config.warning(f'End log for {self._app_name} after {diff} time\n' + '-' * 130)


class Request(Logger):

    def __init__(self, name):
        super().__init__(name=name)
        self._url = 'http://127.0.0.1:5000/erp'

    def req(self, time, am, ty, data=None):
        self._config.critical(f'checking {time} {am} for next process')
        if self.__check(time, am):
            if ty.upper() in ('POST', 'PUT'):
                try:
                    req = requests.request(ty.lower(), url=self._url, data=data)
                    if req.status_code < 400:
                        if ty.upper() == 'POST':
                            self._config.info(f'[POST] {req.url} are add new data {data}')
                        else:
                            self._config.info(f'[PUT] {req.url} update data {data}')
                    else:
                        self._config.error(f'[Error] {req.status_code}')
                except Exception as e:
                    self._config.error(f'[Error] faced {e}')
            else:
                req = requests.request(ty, url=self._url)
        else:
            self._config.critical(f'{time} is less then current time')

    def __check(self, time, am):
        hour, minuts = map(int, time.split(':'))
        if am == 'pm' and hour < 12:
            hour += 12
        time = datetime.strptime(f'{hour}:{minuts}', "%H:%M")
        time2 = datetime.strptime(f'{datetime.now().hour}:{datetime.now().minute}', "%H:%M")
        diff = time - time2
        if str(diff) == '0:00:00':
            return True
        elif diff.days < 0:
            return False
        else:
            h, m, s = str(diff).split(':')

            self._config.warning(
                f'{self._app_name} are wait for {h} hours : {m} minutes : {s} seconds time for start operation')
            while True:
                if hour == datetime.now().hour and minuts == datetime.now().minute:
                    break
            return True

    def __del__(self):
        self._config.warning(f'{self._app_name} are going to logout!\n' + '-' * 130)
        super().__del__()


if __name__ == '__main__':
    r1 = Request('harshit')
    with open('data.json') as f:
        data = json.loads(f.read())[0]
        r1.req(time=data['time'], am=data['am'], ty=data['ty'], data=data['data'])
    # time, am, ty = input('time, am/pm, get/post/put \n>>> ').split(',')
    # data = input('key: value pair or None \n>>> ').split(',')
    # r1.req(time=time, am=am, ty=ty, data=data)