#fixture固件 function class   执行标记：autouse=True
import pytest

@pytest.fixture(scope="class",autouse=True)
def setup_class_fixture():
    print("\nsetup_class_fixture: 这是在测试类开始之前执行的钩子")
    yield 
    print("\nteardown_class_fixture: 这是在测试类结束之后执行的钩子")
