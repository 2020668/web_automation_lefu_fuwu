# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/27

E-mail:keen2020@outlook.com

=================================


"""


import time
import win32gui
import win32con
import re
import jieba


def upload(file_path, browser_type="chrome"):
    if browser_type == "chrome":
        title = "打开"
    else:
        title = ""

    # 找元素
    # 一级窗口 "#32770", "打开"
    dialog = win32gui.FindWindow("#32770", title)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)    # 二级窗口,0代表从第一个开始找,后面是class和title
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)    # 三级窗口
    # 编辑按钮
    edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)       # 四级窗口
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")

    # 往编辑当中输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)     # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)      # 点击打开按钮


def address_match(delivery_addresses):
    if not delivery_addresses:
        return {}
    delivery_addresses = re.sub('[\s,,]+', ',', delivery_addresses).split(",")  # 正则替换
    name, mobile, address = str(), str(), str()
    try:
        name, mobile, address = extract_info(delivery_addresses)
    except:
        pass

    seg_list = jieba.lcut(address, cut_all=False)

    # 去除单个的关键分词(影响查询结果)
    for key in seg_list:
        if key.encode() in ['区', '县', '镇', '乡']:
            seg_list.remove(key)

    # province
    provinces = query('SELECT * FROM area WHERE display=1 AND level=1 AND pid=0;')
    province_dict = {}
    for province in provinces:
        for key in seg_list:
            if key in province.get("name"):
                province_dict = province
                break

    # cities
    if not province_dict:
        cities = query('SELECT * FROM area WHERE display=1 AND level=2;')
    else:
        cities = query(f'SELECT * FROM area WHERE display=1 AND level=2 AND pid={province_dict.get("id")};')
    city_dict = {}
    for city in cities:
        for key in seg_list:
            if key in city.get("name"):
                city_dict = city
                break

    # counties
    if not city_dict:
        counties = query('SELECT * FROM area WHERE display=1 AND level=3;')
    else:
        counties = query(f'SELECT * FROM area WHERE display=1 AND level=3 AND pid={city_dict.get("id")};')
    dis_dict = {}
    index = 0
    for county in counties:
        for key in seg_list:
            if key in county.get("name"):
                dis_dict = county
                index = address.index(key) + 2
    if not dis_dict:
        return {}
    else:
        if not city_dict:
            city = query(f'SELECT * FROM area WHERE id={dis_dict.get("pid")};')
            city_dict = city

        if not province_dict:
            province = query(f'SELECT * FROM area WHERE id={city_dict.get("pid")};')
            province_dict = province
    address_dict = {
        'province': province_dict.get('name'),
        'province_id': province_dict.get('id'),
        'city': city_dict.get('name'),
        'city_id': city_dict.get('id'),
        'county': dis_dict.get('name'),
        'county_id': dis_dict.get('id'),
        'address': address[int(index) + len(key):],
        'mobile': mobile,
        'name': name
    }
    return address_dict


time.sleep(3)
upload("C:\\Users\keen\\Documents\\Software Testing\\Python自动化\\作业\\1831\\12306.py")
# upload("C:\\aow_drv.log")