# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""


from Common.basepage import BasePage
from PageLocators.login_page_locator import LoginPageLocator as loc


class LoginPage(BasePage):

    def login(self,username,passwd):
        self.input_text(loc.user_loc,username,"登陆页面_输入用户名")
        self.input_text(loc.passwd_loc,passwd,"登陆页面_输入密码")
        self.click_element(loc.login_button_loc,"登陆页面_点击登陆按钮")

    def get_form_error_info(self):
        return self.get_text(loc.form_error_loc,"登陆页面_获取登陆表单的错误提示信息")

    # 获取页面中间的提示信息
    def get_page_center_error_info(self):
        return self.get_text(loc.page_center_error_loc,"登陆页面_获取页面中间的错误提示信息")