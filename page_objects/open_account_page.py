# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/25

E-mail:keen2020@outlook.com

=================================


"""

import time
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from page_locators.open_account_page_locator import OpenAccountPageLocator as Loc


class OpenAccountPage(BasePage):

    def open_account(self, account_phone, jy_type, shop_name, shop_nickname, shop_type):

        shop_type_name_loc = By.XPATH, "//li[text()='{}']".format(shop_type)

        self.wait_ele_visible(loc=Loc.phone_input_loc, img_desc="手机号码输入框")
        self.input_text(loc=Loc.phone_input_loc, value=account_phone, img_desc="手机号码输入框")

        self.wait_ele_visible(loc=Loc.next_step_loc, img_desc="下一步按钮")
        self.click_element(loc=Loc.next_step_loc, img_desc="下一步按钮")

        if jy_type == "小微商户":
            self.wait_ele_visible(loc=Loc.xiaowei_loc, img_desc="小微商户的选择按钮")
            self.click_element(loc=Loc.xiaowei_loc, img_desc="小微商户的选择按钮")

            time.sleep(1)

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
            self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="商户全称输入框")

            self.wait_ele_visible(loc=Loc.shop_nickname_input_loc, img_desc="商户简称输入框")
            self.input_text(loc=Loc.shop_nickname_input_loc, value=shop_nickname, img_desc="商户简称输入框")

            self.wait_ele_visible(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.click_element(loc=Loc.shop_type_loc, img_desc="商户类型选择框")
            self.wait_ele_visible(loc=shop_type_name_loc, img_desc="商户类型")
            self.click_element(loc=shop_type_name_loc, img_desc="商户类型")

            self.wait_ele_visible(loc=Loc.shop_area_loc, img_desc="商户地区选择框")
            self.click_element(loc=Loc.shop_area_loc, img_desc="商户地区选择框")

