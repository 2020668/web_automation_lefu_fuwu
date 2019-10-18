#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_invest
# Author: keen
# Time: 2019/8/2

"""
前置：
打开网页\帐号已登陆
帐户有钱 - 在重复的自动化执行时，用户一直有足够的钱投资。> 2900
     1、先充几个亿
     2、直接更新它的钱： 投多少充多少。----接口

有可投的标 -
    1、自己加标，让标处于竞标的状态  ---- 接口
    2、在首页当中，选择最近一次添加的标进行投资

步骤：准备投2000块.range(100,3000)
"""
import unittest
from selenium import webdriver
import logging
import pytest

from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage

from TestDatas import Common_Datas as cd
from TestDatas import invest_datas as ID

# 前置后置 、步骤 、 断言
class TestInvest(unittest.TestCase):

    def setUp(self):
        # 前置 访问网址，并登陆成功
        self.driver = webdriver.Chrome()
        self.driver.get(cd.login_url)
        LoginPage(self.driver).login(cd.user,cd.passwd)
        self.bid_page = BidPage(self.driver)

    def tearDown(self):
        # 后置
        pass

    # @pytest.mark.smoke
    # def test_invest_1_success(self):
    #     logging.info("*********投资用例：正常场景-投资成功*********")
    #     # 标页面 - 获取投资前的个人余额
    #     userMoney_beforeInvest = self.bid_page.get_user_left_money()
    #     # 标页面 - 输入投资金额 ，点击投标按钮
    #     self.bid_page.invest(ID.success["money"])
    #     # 标页面 - 投资成功弹出框 ，点击查看并激活按钮
    #     self.bid_page.click_active_button_on_invest_success_popup()
    #     # #验证
    #     # 个人页面 - 获取用户当前余额
    #     userMoney_afterInvest = UserPage(self.driver).get_user_left_money()
    #     # 1、余额：投资前获取一下，投资后再获取一下。求差值，如果等于投资金额，那正确。
    #     assert ID.success["money"] == int(float(userMoney_beforeInvest) - float(userMoney_afterInvest))
    #     # PS：自动化测试独立帐号。
    #     # 2、个人页面 - 投资记录获取。

    @pytest.mark.slow
    def test_case2(self):
        assert True


