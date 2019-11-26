# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/26
E-mail:keen2020@outlook.com
=================================

"""


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from common import logger


base_url = "https://www.tapd.cn/63534300/bugtrace/bugreports/my_view?filter=true&data[Filter]" \
           "[status][]=verified&qksearch=true&qksearch=true"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url=base_url)
time.sleep(3)

# 用户名输入框
loc = By.XPATH, "//input[@id='username']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("15071366971")
logging.info("用户名输入成功")

# 密码输入框
loc = By.XPATH, "//input[@id='password_input']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("Zuowei19881128")
logging.info("密码输入成功")

# 登录按钮
loc = By.XPATH, "//input[@id='tcloud_login_button']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()
logging.info("点击登录按钮成功")

time.sleep(3)

# 点击所有的
loc = By.XPATH, "//span[@title='所有的']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()
logging.info("点击所有的成功")

# 点击我创建的
loc = By.XPATH, "//a[@title='我创建的']"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()
logging.info("点击我创建的成功")

# # 过滤按钮
# loc = By.XPATH, "//span[@class='filter-text filter-text_active']"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
# logging.info("点击过滤按钮成功")
#
# # 勾选已验证
# loc = By.XPATH, "//label[@title='已验证']"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
# logging.info("点击已验证成功")
#
# # 过滤按钮
# loc = By.XPATH, "//a[@id='do_filter']"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
# logging.info("点击过滤按钮成功")


i = 0
while i < 130:
    loc = By.XPATH, "//span//a"

    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()
    logging.info("点击Bug标题成功")

    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 650); ")
    logging.info("向下滑动成功")

    loc = By.XPATH, '//label[@for="status_closed"]'
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()
    logging.info("点击已关闭成功")

    loc = By.XPATH, "//a[@id='update_status_btn']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()
    logging.info("点击流转成功")

    loc = By.XPATH, "//li[@class='brick current']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()
    logging.info("点击缺陷成功")

    i += 1
    logging.info("第")
