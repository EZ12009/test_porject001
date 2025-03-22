import requests
import os

class Requestutil :

    sess = requests.session()
    # 封装请求
    def all_send_request(self, **kwargs):
        res = Requestutil.sess.request(**kwargs)
        # print(kwargs["params"])
        # print(res.text)
        return res

