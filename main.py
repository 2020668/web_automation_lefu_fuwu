# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

import pytest
import os


"""
参数 -s 允许终端运行时输出某些结果，例如pri
-v 输出详细测
-m 只运行指定标签名的测
-x 报错时停止
"""
pytest.main(
    ["-s", "-x", "-m", "login", "--html=outputs/reports/report.html", "--alluredir=outputs/allure"])

# 直接打开报告
os.system("allure serve outputs/allure")
