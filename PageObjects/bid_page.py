#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: bid_page
# Author: 简
# Time: 2019/8/5

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.bidPage_locator import BidPageLocator as loc

class BidPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_left_money(self):
        # 等待元素可见
        # 操作
        pass

    # 投资操作
    def invest(self, money):
        # 等待元素可见
        # 操作
        pass

    # 在投资成功的窗口中 - 点击查看并激活
    def click_active_button_on_invest_success_popup(self):
        # 等待元素可见
        # 操作
        pass