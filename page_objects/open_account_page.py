# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/25

E-mail:keen2020@outlook.com

=================================


"""

from common.basepage import BasePage
from page_locators.open_account_page_locator import OpenAccountPageLocator as Loc


class OpenAccountPage(BasePage):

    def open_account(self, account_phone, jy_type):

        self.wait_ele_visible(loc=Loc.phone_input_loc, img_desc="手机号码输入框")
        self.input_text(loc=Loc.phone_input_loc, value=account_phone, img_desc="手机号码输入框")

        self.wait_ele_visible(loc=Loc.next_step_loc, img_desc="下一步按钮")
        self.click_element(loc=Loc.next_step_loc, img_desc="下一步按钮")

        if jy_type == "小微商户":
            self.wait_ele_visible(loc=Loc.xiaowei_loc, img_desc="小微商户的选择按钮")
            self.click_element(loc=Loc.xiaowei_loc, img_desc="小微商户的选择按钮")

            self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="商户全称输入框")
