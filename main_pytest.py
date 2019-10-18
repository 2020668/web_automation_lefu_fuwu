#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main_pytest
# Author: 简
# Time: 2019/8/7
import pytest

if __name__ == '__main__':
    pytest.main(["-s","-v","-m","slow"])

# 注册标签名  pytest.ini
# 给用例打标签：@pytest.mark.注册的标签名
# 根据标签名过滤要运行的用例：-m 标签名


