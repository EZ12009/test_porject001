import os
import yaml

# 获取当前工作目录下的文件路径
def find_file_in_current_directory(filename):
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 遍历当前目录及其所有子目录
    for dirpath, dirnames, filenames in os.walk(current_directory):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None
extract_name = 'extract.yaml'
# yaml_file_path = os.path.join(os.getcwd(), "extract.yaml")
yaml_file_path = find_file_in_current_directory(extract_name)


# 写入 YAML 数据
def write_yaml(data):
    try:
        with open(yaml_file_path, encoding="utf-8", mode="a+") as f:  # 使用 'w' 模式覆盖写入 'a+' 
            yaml.dump(data, stream=f, allow_unicode=True, default_flow_style=False)
        print("数据已成功写入 YAML 文件")
    except Exception as e:
        print(f"写入 YAML 文件失败: {e}")

# 读取 YAML 数据
def read_yaml(key):
    try:
        with open(yaml_file_path, encoding="utf-8", mode="r") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value.get(key, None)  # 使用 get() 方法避免 KeyError
    except FileNotFoundError:
        print("YAML 文件不存在1")
        return None
    except yaml.YAMLError as e:
        print(f"YAML 文件格式错误: {e}")
        return None
    except Exception as e:
        print(f"读取 YAML 文件失败: {e}")
        return None

#清空文件 f.truncate()


def clear_yaml(yaml_file_path):
    try:
        # 以写模式打开文件，清空内容
        with open(yaml_file_path, encoding="utf-8", mode="w") as f:
            # 如果文件打开成功，直接关闭，文件内容被清空
            pass #这里可以替换为f.truncate()双重清空
    except FileNotFoundError:
        print("YAML 文件不存在2")
        return None
    except OSError as e:
        print(f"文件操作失败: {e}")
        return None
    except Exception as e:
        print(f"清空 YAML 文件时发生错误: {e}")
        return None
    
# 读取 测试用例 数据
def read_testcase_yaml(filename):
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 在当前工作目录及其所有子目录中查找文件
    for dirpath, dirnames, filenames in os.walk(current_directory):
        if filename in filenames:
            testcase_file_path = os.path.join(dirpath, filename)
            break
    else:
        print(f"文件 '{filename}' 不存在")
        return None

    # 读取 YAML 文件
    try:
        with open(testcase_file_path, encoding="utf-8", mode="r") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value
    except yaml.YAMLError as e:
        print(f"YAML 文件格式错误: {e}")
        return None
    except Exception as e:
        print(f"读取 YAML 文件失败: {e}")
        return None