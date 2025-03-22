from commons.request_util import Requestutil
from commons.yaml_util import write_yaml,read_yaml
import requests
import pytest


class Test_imbp_valid_domains_api:
    
    #1、食物热量
    def test_calories(self):
        url = "http://shanhe.kim/api/za/calories.php?food=苦瓜"
        params = {"food": "苦瓜"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=params)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            #写入yaml文件
            # host_datas = {'host_list': Requestutil().generate_valid_domains(10)}
            # write_yaml(host_datas)
        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e},url:{url}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")
        
     #2 微博热搜榜
    def test_goto_index(self):
        url = 'http://shanhe.kim/api/za/weibo.php'
        res = Requestutil().all_send_request(method='get',url=url,params=None)
        print(res.text)
    