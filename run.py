import pytest
import os
import time

if __name__ == "__main__" :
    pytest.main()
    time.sleep(1)
    # 调用allure生成报告
    os.system("allure generate ./temps -o ./reports001 --clean")
    # 自动打开报告·
    # os.system("allure open ./reports001 ")
