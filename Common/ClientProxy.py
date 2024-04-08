"""
@author:Liuyiling
@description:
@date:2024/3/28 15:05

"""
import json
import logging


class ClientProxy:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        attr = getattr(self._target, name)
        if callable(attr):
            return self._wrap_method(attr)
        else:
            return attr

    # def __setattr__(self, name, value):
    #     if name == "_target":
    #         super().__setattr__(name, value)
    #     else:
    #         setattr(self._target, name, value)

    def _wrap_method(self, method):
        def wrapped_method(obj):
            # Log method call and arguments
            # 换行
            print('=============================')
            print(f"Calling method: {method.__name__}")
            print(f"请求参数: \n{obj}")
            result = method(obj)
            print(f"返回参数: \n{result}")
            print('=============================')

            return result

        return wrapped_method
