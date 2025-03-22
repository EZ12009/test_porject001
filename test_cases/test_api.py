
from commons.request_util import Requestutil
from commons.yaml_util import write_yaml,read_yaml,read_testcase_yaml
import requests
import pytest
import jsonpath


# 将错误信息写入文件的函数
def log_error_to_file(message, filename='test_errors.log'):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

class Test_imbp_api:
    
    #针对每个拥挤执行钩子函数推荐使用 setup_method 和 teardown_method 类：setup_class 和 teardown_class
    # def setup_method(self) :
    #     print("前置处理逻辑（用例请求之前，如数据库连接）")
    # def teardown_method(self) :
    #     print("后置置处理逻辑（用例请求之后，如数据库关闭）")
    
    
    # 1 获取手机信息
    
    def test_Home_of_the_mobile_phone_number(self):
        url = "http://shanhe.kim/api/za/phone.php"
        params = {"tel": "15209758144"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=params)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            # 提取 'type' 值 后（#构建全局变量字典,提取数据并写入）
            value = jsonpath.jsonpath(result,'$.type')
            # Test_imbp_api.local_value = result.get("type", "未定义")  # 存储到类变量中(老方案)
            # print(f"获取的 local_value: {Test_imbp_api.local_value}")
            
            datas = {'local_value' :value[0]}
            write_yaml(datas)
        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")

    # 2 时间段模糊一言
    @pytest.mark.parametrize('casedata2',read_testcase_yaml('funny_quote.yaml'))
    def test_time_period_vague_word(self,casedata2):
        url = casedata2.get('request', {}).get('url', None)
        method = casedata2.get('request', {}).get('method', None)
        params = casedata2.get('request', {}).get('params', {})
        for key,value in params.items():
            params[key] = read_yaml(key)
        #接口关联测试
        # new_local = read_yaml('local_value')
        print(f'#####关联后数据传参#######：{params}')
        
            
            

        try:
            res = Requestutil().all_send_request(method=method, url=url, params=None)
            print(res.text)
            result = res.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")

    # 3 获取票房信息
    @pytest.mark.smoke
    def test_Box_office_enquiries_across_the_net(self):
        url = "http://shanhe.kim/api/za/piaofang.php"
        
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=None)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            # 提取 '' 值
            day_value = result.get('day','data_time')
            top1_name = result.get("Top_1", {}).get("name","默认名称")
            # print(f"获取的 NUM_1: 当前查询时间：{day_value},票房第一名为：{top1_name}")

        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")
    # 4 人生倒计时

    def test_countdown_to_life(self):
        url = "http://shanhe.kim/api/za/rsdjs.php"
        params = {"type": "jsom"}
        try:
            # 发起请求
            res = Requestutil().all_send_request(method="get", url=url, params=params)
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
    
    # 5每日英语
    @pytest.mark.parametrize('casedata1',read_testcase_yaml('test_get_everyday_english.yaml'))
    def test_everyday_english(self,casedata1):
        
        url = casedata1.get('request', {}).get('url', None)
        method = casedata1.get('request', {}).get('method', None)
        params = casedata1.get('request', {}).get('data', {})
        headers = casedata1.get('request', {}).get('headers', {})
        try:
            # 发起请求
            res = Requestutil().all_send_request(method=method, url=url,headers=headers,data=params)
            # 确保请求成功
            res.raise_for_status()  # 如果返回的状态码不是 200，会引发 HTTPError
            # 尝试解析 JSON
            result = res.json()
            # 检查返回的 JSON 是否包含 'reason' 和 'success'
            assert result.get('reason') == 'success', f'返回数据存在异常，打印原数据：{result}'
            assert "result" in result, f'返回数据中缺少result字段，打印原数据：{result}'
            # 进一步检查 result 内的字段
            content = result['result'].get('content', '')
            note = result['result'].get('note', '')
            assert content and note, f'内容或注释缺失，返回数据：{result}'
            # 动态执行测试数据中的 validate 断言
            # for validate_statement in casedata.get('validate', []):
            #     try:
            #         # 使用 eval 执行 assert 语句
            #         eval(validate_statement.format(result=result))
            #     except AssertionError as e:
            #         error_message = f"验证失败: {str(e)}"
            #         log_error_to_file(error_message)  # 使用 log_error_to_file 函数来记录错误
            #         raise
        except requests.exceptions.RequestException as e:
            # 处理请求异常，例如连接错误、超时等
            print(f"请求错误: {e}")
        except ValueError as e:
            # 处理 JSON 解析错误
            print(f"JSON 解析错误: {e}")
        except KeyError as e:
            # 处理键不存在错误
            print(f"键错误: {e}")
    