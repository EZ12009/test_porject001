#fixture固件 function class  session  执行标记：autouse=True
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'commons')))
import pytest
from yaml_util import clear_yaml



params = ['白羊','双鱼','天秤'] #参数化
@pytest.fixture(scope="function",autouse=False,params=params)
def setup_function_fixture(request):
    print("\nsetup_function_fixture: 这是在测试用例1开始之前执行的钩子")
    yield request.param
    print("\nteardown_function_fixture: 这是在测试用1例结束之后执行的钩子")


# 获取当前工作目录下的文件路径
yaml_file_path = os.path.join(os.getcwd(), "extract.yaml")
host_list = ['hunan.gov.cn','csdn.net','hxsd.com','yunnan.cn','changsha.gov.cn','shanhe.kim','apis.juhe.cn']
@pytest.fixture(scope="class",autouse=False,params=host_list)
def setup_host_list(request):
    
    clear_yaml(yaml_file_path)
    yield request.param
    print("\nteardown_function_fixture: 这是在测试用2例结束之后执行的钩子")
