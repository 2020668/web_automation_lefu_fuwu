# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

import unittest
from selenium import webdriver
import ddt
import logging
import pytest
import time

from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from page_objects.open_account_page import OpenAccountPage

from data import common_data as cd
from data import open_account_data as od


# 测试用例 = 测试对象的功能 + 测试数据
@ddt.ddt
@pytest.mark.login  # 给整个测试类打标记。类下的所有测试用例，都带有这个标记。
class OpenAccount(unittest.TestCase):

    def setUp(self):
        logging.info("==========登陆功能中每个用例的前置：打开浏览器，访问网址=============")
        # 打开浏览器，访问网址
        self.driver = webdriver.Chrome()
        self.driver.get(cd.login_url)
        self.driver.maximize_window()

    def tearDown(self):
        logging.info("==========登陆功能中每个用例的后置：关闭浏览器会话=============")
        self.driver.quit()

    @pytest.mark.parametrize("data", od.success_data)
    def test_open_account_success(self, data):
        # 用例 = 登陆页的登陆功能 - 首页的 检查用户昵称存在的功能

        # 步骤
        LoginPage(self.driver).login_action("18627787716", "123456")

        time.sleep(2)

        # 点击开户进件
        IndexPage(self.driver).click_open_account()

        # 执行开户进件
        OpenAccountPage(self.driver).open_account(account_phone=data["account_phone"],
                                                  jy_type=data["jy_type"],
                                                  shop_name=data["shop_name"],
                                                  shop_nickname=data["shop_nickname"],
                                                  shop_type=data["shop_type"],
                                                  area=data["area"],
                                                  address=data["address"],
                                                  rate=data["rate"],
                                                  pos=data["pos"],
                                                  debit_card_rate=data["debit_card_rate"],
                                                  credit_card_rate=data["credit_card_rate"],
                                                  js_name=data["js_name"],
                                                  sf_id=data["sf_id"],
                                                  e_mail=data["e_mail"],
                                                  alipay_name=data["alipay_name"],
                                                  alipay_account=data["alipay_account"],
                                                  wechat_account=data["wechat_account"],
                                                  company_name=data["company_name"],
                                                  bank_card=data["bank_card"],
                                                  bank_address=data["bank_address"],
                                                  bank_name=data["bank_name"],
                                                  zhi_bank_name=data["zhi_bank_name"],
                                                  people_address=data["people_address"]
                                                  )
