# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/18
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.userPage_locator import UserPageLocator as loc


class UserPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取用户的余额
    def get_user_left_money(self):
        pass

    # 获取第一条投资记录(标名、金额)
    def get_first_invest_record(self):
        pass

