#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: 简
# Time: 2019/7/31

import unittest
from selenium import webdriver
import ddt
import logging
import pytest

from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage

from TestDatas import Common_Datas as cd
from TestDatas import login_datas as ld

# 测试用例 = 测试对象的功能 + 测试数据
@ddt.ddt
@pytest.mark.login   # 给整个测试类打标记。类下的所有测试用例，都带有这个标记。
class TestLogin(unittest.TestCase):

    def setUp(self):
        logging.info("==========登陆功能中每个用例的前置：打开浏览器，访问网址=============")
        # 打开浏览器，访问网址
        self.driver = webdriver.Chrome()
        self.driver.get(cd.login_url)
        self.driver.maximize_window()

    def tearDown(self):
        logging.info("==========登陆功能中每个用例的后置：关闭浏览器会话=============")
        self.driver.quit()

    @pytest.mark.smoke
    def test_login_success(self):
        # 用例 = 登陆页的登陆功能 - 首页的 检查用户昵称存在的功能
        # 步骤
        LoginPage(self.driver).login(ld.success["user"],ld.success["passwd"])
        # 断言
        self.assertTrue(IndexPage(self.driver).check_userName_exists())

    @ddt.data(*ld.invalid_datas)
    def test_login_noPasswd(self,data):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login(data["user"], data["passwd"])
        # 断言
        self.assertEqual(data["check"],lp.get_form_error_info())

    def test_login_wrongPasswd(self):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login("18684720000", "python")
        # 断言
        self.assertEqual("此账号没有经过授权，请联系管理员!",lp.get_page_center_error_info())

    @pytest.mark.slow
    def test_case1(self):
        assert True