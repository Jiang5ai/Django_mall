# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 20:38
# @Author  : JS
# @File    : constants.py
# @Software: PyCharm

# 系统模块-轮播图配置
SLIDER_TYPE_INDEX = 11
SLIDER_TYPES_CHOICES = (
    (SLIDER_TYPE_INDEX, '首页'),
)

# 系统模块-新闻通知
NEWS_TYPE_NEW = 11
NEWS_TYPES_NOTICE = 12
NEWS_TYPES_CHOICES = (
    (NEWS_TYPE_NEW, '新闻'),
    (NEWS_TYPES_NOTICE, '通知')
)

# 商品模块-商品类型
PRODUCT_TYPE_ACTUAL = 11
PRODUCT_TYPE_VIRTUAL = 12
PRODUCT_TYPE_CHOICES = (
    (PRODUCT_TYPE_ACTUAL, '实物商品'),
    (PRODUCT_TYPE_VIRTUAL, '虚拟商品')
)

# 商品模块-商品状态
PRODUCT_STATUS_SELL = 11
PRODUCT_STATUS_LOST = 12
PRODUCT_STATUS_OFF = 13
PRODUCT_STATUS_CHOICES = (
    (PRODUCT_STATUS_SELL, '销售中'),
    (PRODUCT_STATUS_LOST, '已售完'),
    (PRODUCT_STATUS_OFF, '已下架'),

)
