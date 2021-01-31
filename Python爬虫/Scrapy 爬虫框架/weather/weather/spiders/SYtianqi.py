#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
# 别忘了，将item导入进来，这样数据才能在各个模块之间流转
from weather.ites import WeatherItem

class SytianqiSpider(scrapy.Spider):
    name = 'SYtianqi'

    # 我们修改一下host，使得Scrapy可以爬取除了苏州之外的天气
    allowed_domains = ['tianqi.com']

    # 建立需要爬取信息的url列表
    start_urls = []

    # 需要爬的城市名称 可以自行添加
    citys = ['shiyan', 'suzhou', 'shanghai']

    # 用一个很简答的循环来生成需要爬的链接：
    for city in citys:
        start_urls.append('http://tianqi.com/{}'.format(city))


    def parse(self, response):
        '''
        筛选信息的函数：
        date = 今日日期
        week = 星期几
        img = 表示天气的图标
        temperature = 当天的温度
        weather = 当天的天气
        wind = 当天的风向
        '''

        # 先建立一个列表，用来保存每天的信息
        items = []

        # 找到包裹着每天天气信息的div
        sevneday = response.xpath('//div[@class="day7"]')

        # 循环筛选出每天的信息：
        for day in sevneday:
            # 先申请一个weatheritem 的类型来保存结果
            item = WeatherItem()

            # 观察网页，知道h3标签下的不单单是一行str，我们用trick的方式将它连接起来
            date = ''
            for datetitle in day.xpath()