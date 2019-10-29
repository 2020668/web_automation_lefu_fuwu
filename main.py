# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-v"])
# 注册标签名  pytest.ini
# 给用例打标签：@pytest.mark.注册的标签名
# 根据标签名过滤要运行的用例：-m 标签名
