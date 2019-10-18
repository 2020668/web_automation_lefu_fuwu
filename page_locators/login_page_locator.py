# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (By.XPATH, '//button')
    # 表单错误提示
    form_error_loc = (By.XPATH, '//div[@class="form-error-info"]')
    # 页面中间错误提示
    page_center_error_loc = (By.XPATH, '//div[@class="layui-layer-content"]')
