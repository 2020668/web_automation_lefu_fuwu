# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/25

E-mail:keen2020@outlook.com

=================================


"""


from selenium.webdriver.common.by import By


class OpenAccountPageLocator(object):

    # 手机号码输入框
    phone_input_loc = By.XPATH, "//input[@placeholder='请输入商户的手机号码']"

    # 测试管理员294（自己）
    self_loc = By.XPATH, "//label[text()= ('测试管理员294（自己）')]"

    # 其他合伙人人
    other_loc = By.XPATH, "//label[text()= ('其它合伙人')]"

    # 下一步
    next_step_loc = By.XPATH, "//span[text()= ('下一步')]"

    # 小微商户
    xiaowei_loc = By.XPATH, "//p[text()=('小微商户')]//following-sibling::p[text()='选择']"

    # 个体工商，结算同法人
    geti_same_loc = By.XPATH, "//p[text()=('个体工商户-结算同法人')]//following-sibling::p[text()='选择']"

    # 个体工商，结算非法人
    geti_different_loc = By.XPATH, "//p[text()=('个体工商户-结算同法人')]//following-sibling::p[text()='选择']"

    # 企业对公
    qiye_loc = By.XPATH, "//p[text()=('企业对公')]//following-sibling::p[text()='选择']"

    # 企业对私 结算同法人
    qiye_geti_same_loc = By.XPATH, "//p[text()=('企业对私-结算同法人')]//following-sibling::p[text()='选择']"

    # 企业对私 结算非法人
    qiye_geti_different_loc = By.XPATH, "//p[text()=('企业对私-结算非法人')]//following-sibling::p[text()='选择']"

