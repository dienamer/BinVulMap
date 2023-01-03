global _global_information_dict_  ##初始化一个全局变量
_global_information_dict_={}

# 初始化
def init():
    global _global_information_dict_
    _global_information_dict_ = {}


# 赋值
def set_value(key, value):
    _global_information_dict_[key] = value


# 获取值
def get_value(key):
    return _global_information_dict_[key]
