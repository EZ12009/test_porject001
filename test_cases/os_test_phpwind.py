import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'commons')))
from request_util import Requestutil
import requests
import pytest
 

class Test_imbp_order_view_api:
    
    # 1 历史上的今天
    @pytest.mark.product_manage
    def test_Today_history(self):
        url = "http://shanhe.kim/api/za/lishi.php"
        params = {"format": "json"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=params)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            # 提取 'type' 值
            # Test_imbp_api.local_value = result.get("type", "默认值")  
            # print(f"获取的 local_value: {Test_imbp_api.local_value}")
            # assert 'pass' == 'add'
        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e},url:{url}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")
        
    # 2 神回复信息
    @pytest.mark.smoke
    def test_recover_message(self):
        url = "http://shanhe.kim/api/za/shenhuifu.php"
        params = {"type": "json"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=None)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
        

        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")
    # 3 星座信息
    
    def test_star_sign_message(self,setup_function_fixture):
        print(setup_function_fixture)
        url = "http://shanhe.kim/api/za/xingzuo.php"
        params = {"msg":setup_function_fixture,"type": "json"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=params)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            print(result)

        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")
    
    # 4 端口扫描
    @pytest.mark.get_hose_inquire
    def test_star_sign_message(self,setup_host_list):
        print(f'域名参数化结果：{setup_host_list}')
        url = "http://shanhe.kim/api/wz/duanko.php"
        params = {"host":setup_host_list,"type": "json"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=params)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            port_21_status = result['port'].get('21', None)

            assert port_21_status == '关闭', f"端口 21 当前状态为: {port_21_status}"

        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")


