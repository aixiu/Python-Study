#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get('http://www.baidu.com')

print(r.request.headers)   # HTTP请求头
print(r.headers)  #HTTP响应头
print(r.status_code)  #HTTP请求的返回状态，比如，200表示成功，404表示失败
print(r.encoding)  #从header中猜测的响应的内容编码方式 
print(r.apparent_encoding)  #从内容中分析的编码方式（慢）

print(r.text)  #响应内容的Unicode型的数据
print(r.content)  #响应内容的二进制形式

## 区别：

# resp.text返回的是Unicode型的数据。
# resp.content返回的是bytes型也就是二进制的数据。

    # 也就是说，如果你想取文本，可以通过r.text。
    # 如果想取图片，文件，则可以通过r.content。
    # （resp.json()返回的是json格式数据）


# requests抓取网页的通用框架

import requests

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=20)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Something Wrong!'


# 本文链接：https://zhuanlan.zhihu.com/p/26681429


# 给出一个图片下载的通用代码片段：

    import requests
    
    def get_pic_from_url(url):
        #从url以二进制的格式下载图片数据
        pic_content = requests.get(url,stream=True).content
        open('filename','wb').write(pic_content)

# 本文链接：https://zhuanlan.zhihu.com/p/26786056