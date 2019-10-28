# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/12

E-mail:keen2020@outlook.com

=================================


"""

success_data = [
    {"account_phone": "18911110069",
     "msg_code": "123456",
     "jy_type": "小微商户",
     "credit_code": "None",
     "shop_name": "长安同福客栈69",
     "shop_nickname": "同福客栈69",
     "shop_type": "医疗健康",
     "area": "内蒙古呼和浩特市新城区",
     "address": "内蒙古呼和浩特市新城区特1号",
     "rate": 0.45,
     "pos": True,
     "debit_card_rate": "2.50",
     "credit_card_rate": "2.52",
     "js_type": "None",
     "corporate_name": "None",
     "corporate_id": "None",
     "js_name": "张秀才",
     "sf_id": "420114199010025829",
     "e_mail": "23634266@qq.com",
     "alipay_name": "张秀才",
     "alipay_account": "18911112222",
     "wechat_account": "ls2002",
     "company_name": "None",
     "bank_card": "6236682950005948000",
     "bank_name": "中国建设银行",
     "bank_address": "北京市东城区",
     "zhi_bank_name": "中国建设银行北京外国语大学支行",
     "people_address": "湖北省武汉市武昌区徐家棚街道特1号"},
    # {"account_phone": "18911110063",
    #  "msg_code": "123456",
    #  "jy_type": "个体工商",
    #  "credit_code": "92430406MA4Q28027X",
    #  "shop_name": "长安同福客栈63",
    #  "shop_nickname": "同福客栈63",
    #  "shop_type": "医疗健康",
    #  "area": "内蒙古呼和浩特市新城区",
    #  "address": "内蒙古呼和浩特市新城区特1号",
    #  "rate": 0.33,
    #  "pos": True,
    #  "debit_card_rate": "2.50",
    #  "credit_card_rate": "2.52",
    #  "js_type": "结算同法人",
    #  "corporate_name": "None",
    #  "corporate_id": "None",
    #  "js_name": "张秀才",
    #  "sf_id": "420114199010025829",
    #  "e_mail": "23634266@qq.com",
    #  "alipay_name": "张秀才",
    #  "alipay_account": "18911112222",
    #  "wechat_account": "ls2002",
    #  "company_name": "None",
    #  "bank_card": "6236682950005948000",
    #  "bank_name": "中国建设银行",
    #  "bank_address": "北京市东城区",
    #  "zhi_bank_name": "中国建设银行北京外国语大学支行",
    #  "people_address": "湖北省武汉市武昌区徐家棚街道特1号"},
    # {"account_phone": "18911110064",
    #  "msg_code": "123456",
    #  "jy_type": "个体工商",
    #  "credit_code": "92430406MA4Q28027X",
    #  "shop_name": "长安同福客64",
    #  "shop_nickname": "同福客栈64",
    #  "shop_type": "医疗健康",
    #  "area": "内蒙古呼和浩特市新城区",
    #  "address": "内蒙古呼和浩特市新城区特1号",
    #  "rate": 0.28,
    #  "pos": True,
    #  "debit_card_rate": "2.50",
    #  "credit_card_rate": "2.52",
    #  "corporate_name": "佟掌柜",
    #  "corporate_id": "420114199010025820",
    #  "js_type": "结算非法人",
    #  "js_name": "张秀才",
    #  "sf_id": "420114199010025829",
    #  "e_mail": "23634266@qq.com",
    #  "alipay_name": "张秀才",
    #  "alipay_account": "18911112222",
    #  "wechat_account": "ls2002",
    #  "company_name": "None",
    #  "bank_card": "6236682950005948000",
    #  "bank_name": "中国建设银行",
    #  "bank_address": "北京市东城区",
    #  "zhi_bank_name": "中国建设银行北京外国语大学支行",
    #  "people_address": "湖北省武汉市武昌区徐家棚街道特1号"},
    # {"account_phone": "18911110065",
    #  "msg_code": "123456",
    #  "jy_type": "企业对公",
    #  "credit_code": "92430406MA4Q28027X",
    #  "shop_name": "长安同福客栈六五",
    #  "shop_nickname": "同福客栈65",
    #  "shop_type": "医疗健康",
    #  "area": "内蒙古呼和浩特市新城区",
    #  "address": "内蒙古呼和浩特市新城区特1号",
    #  "rate": 0.38,
    #  "pos": True,
    #  "debit_card_rate": "2.50",
    #  "credit_card_rate": "2.52",
    #  "corporate_name": "佟掌柜",
    #  "corporate_id": "420114199010025820",
    #  "js_type": "结算非法人",
    #  "js_name": "张秀才",
    #  "sf_id": "420114199010025829",
    #  "e_mail": "23634266@qq.com",
    #  "alipay_name": "张秀才",
    #  "alipay_account": "18911112222",
    #  "wechat_account": "ls2002",
    #  "company_name": "长安同福客栈六五",
    #  "bank_card": "6236682950005948000",
    #  "bank_name": "中国农业银行海口港口支行",
    #  "bank_address": "北京市东城区",
    #  "zhi_bank_name": "中国建设银行北京外国语大学支行",
    #  "people_address": "湖北省武汉市武昌区徐家棚街道特1号"},
    # {"account_phone": "18911110066",
    #  "msg_code": "123456",
    #  "jy_type": "企业对私",
    #  "credit_code": "92430406MA4Q28027X",
    #  "shop_name": "长安同福客栈66",
    #  "shop_nickname": "同福客栈66",
    #  "shop_type": "医疗健康",
    #  "area": "内蒙古呼和浩特市新城区",
    #  "address": "内蒙古呼和浩特市新城区特1号",
    #  "rate": 0.42,
    #  "pos": True,
    #  "debit_card_rate": "2.11",
    #  "credit_card_rate": "2.52",
    #  "corporate_name": "None",
    #  "corporate_id": "None",
    #  "js_type": "结算同法人",
    #  "js_name": "张秀才",
    #  "sf_id": "420114199010025829",
    #  "e_mail": "23634266@qq.com",
    #  "alipay_name": "张秀才",
    #  "alipay_account": "18911112222",
    #  "wechat_account": "ls2002",
    #  "company_name": "None",
    #  "bank_card": "6236682950005948000",
    #  "bank_name": "中国建设银行",
    #  "bank_address": "北京市东城区",
    #  "zhi_bank_name": "中国建设银行北京外国语大学支行",
    #  "people_address": "湖北省武汉市武昌区徐家棚街道特1号"},
    # {"account_phone": "18911110067",
    #  "msg_code": "123456",
    #  "jy_type": "企业对私",
    #  "credit_code": "92430406MA4Q28027X",
    #  "shop_name": "长安同福客栈67",
    #  "shop_nickname": "同福客栈67",
    #  "shop_type": "医疗健康",
    #  "area": "内蒙古呼和浩特市新城区",
    #  "address": "内蒙古呼和浩特市新城区特1号",
    #  "rate": 0.40,
    #  "pos": True,
    #  "debit_card_rate": "2.50",
    #  "credit_card_rate": "2.52",
    #  "corporate_name": "佟掌柜",
    #  "corporate_id": "420114199010025820",
    #  "js_type": "结算非法人",
    #  "js_name": "张秀才",
    #  "sf_id": "420114199010025829",
    #  "e_mail": "23634266@qq.com",
    #  "alipay_name": "张秀才",
    #  "alipay_account": "18911112222",
    #  "wechat_account": "ls2002",
    #  "company_name": "None",
    #  "bank_card": "6236682950005948000",
    #  "bank_name": "中国建设银行",
    #  "bank_address": "北京市东城区",
    #  "zhi_bank_name": "中国建设银行北京外国语大学支行",
    #  "people_address": "湖北省武汉市武昌区徐家棚街道特1号"}
]