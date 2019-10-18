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
from selenium.webdriver.support import expected_conditions as ec

from page_locators.indexPage_locator import IndexPageLocator as Loc


class IndexPage:
    # 用户昵称定位
    user_loc = (By.XPATH, '//a[contains(text(),"我的帐户")]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_username_exists(self):
        try:
            WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(self.user_loc))
            return True
        except:
            return False

    # 获取标名 - 第一个标
    def get_bid_name(self):
        # 等待
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(Loc.bid_name))
        return self.driver.find_element(*Loc.bid_name).text

    # 点击第一个标的抢投标按钮
    def click_first_bid(self):
        # 等待
        WebDriverWait(self.driver,20).until(ec.visibility_of_element_located(Loc.bid_button))
        self.driver.find_element(*Loc.bid_button).click()
        return self
