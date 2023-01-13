import requests, logging
from datetime import datetime


class Utility:

    def __init__(self, user):
        self.__user = user
        self._req = None
        self._log = self.__config
        self._log.info(f'{self.__user} Login\n'+'-'*130)

    @property
    def __config(self):
        log_format = '[%(asctime)s]  %(message)s'
        logging.basicConfig(format=log_format, level=logging.DEBUG)
        return logging.getLogger(self.__user)

    def get_req(self, hour, mint, am, **kwargs):
        op = self.__check_time(hour, mint, am)
        self._log.warning(f'[get_req] method called')

        if op:
            self._req = requests.get('http://127.0.0.1:5000/erp', params=kwargs)
        else:
            self._log.error(f'get request not call because time is less to current time')

    def post_req(self, hour, mint, am, data: dict):
        op = self.__check_time(hour, mint, am)
        self._log.warning(f'[get_req] method called')
        if op:
            # self._log.info(f'[GET] get request call for {self.__get_url}')
            self._req = requests.post('http://127.0.0.1:5000/erp', data=data)
            if self._req.status_code >= 400:
                pass
                # self._log.error(f'[GET] get request called failed for \n {self.__get_url} with status code {self._req.status_code}')
            else:
                # self._log.info(f'[GET] get request called successfully for \n {self.__get_url} with status code {self._req.status_code}')
                return self._req.json()['form']
        else:
            self._log.error(f'get request not call because time is less to current time')

    def pul_req(self, data: dict, **kwargs):
        self._req = requests.put('http://127.0.0.1:5000/emp-detail/', data=data, params=kwargs)
        return self._req.status_code

    # def delete_req(self, data: dict, **kwargs):
    #     self._req = requests.delete(self.__post_url, data=data, params=kwargs)
    #     return self._req.status_code, self._req.json()['form']

    @staticmethod
    def __check_time(hour, mint, am):
        if am == 'pm':
            hour += 12

        if hour >= datetime.now().hour:
            if mint < datetime.now().minute:
                return False
            else:
                while True:
                    if hour == datetime.now().hour and mint == datetime.now().minute:
                        return True
        else:
            return False

    def __del__(self):
        self._log.info(f'{self.__user} logout\n'+'-'*130)


if __name__ == '__main__':
    c1 = Utility('harry')
    c1.get_req(5, 34, 'pm')
    # c1.post_req()
