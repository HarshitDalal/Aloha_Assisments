import requests


class Utility:

    def __init__(self):
        self._req = None
        self.__get_url = 'http://httpbin.org/get'
        self.__post_url = 'http://httpbin.org/post'
        self.__delete_url = 'http://httpbin.org/delete'
        self.__put_url = 'http://httpbin.org/put'
        self.__patch_url = 'http://httpbin.org/patch'

    def get_req(self, **kwargs):
        self._req = requests.get(self.__get_url, params=kwargs)
        return self._req.status_code, self._req.json()

    def post_req(self, **kwargs):
        self._req = requests.post(self.__post_url, json=kwargs)
        return self._req.status_code, self._req.json()

    def pul_req(self):
        pass

    def delete_req(self):
        pass

    def punch_req(self):
        pass


if __name__ == '__main__':
    c1 = Utility()
    print(c1.post_req(name='harshit', age=23))
