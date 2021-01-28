'''
爬取最新电影排行榜单
url：http://dianying.2345.com/top/
使用 requests --- bs4 线路
Python版本： 3.6
OS： mac os 12.12.4
'''

import requests
import bs4


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        # 该网站采用gbk编码！
        r.encoding = 'gbk'
        return r.text
    except:
        return "someting wrong"


def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    
    # 找到电影排行榜的ul列表
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')
    
    for top in movies:
        #找到图片连接，
        img_url=top.find('img')['src']
        

        name = top.find('span',class_='sTit').a.text
        #这里做一个异常捕获，防止没有上映时间的出现
        try:
            time = top.find('span',class_='sIntro').text
        except:
            time = "暂无上映时间"
        
        #这里用bs4库迭代找出“pACtor”的所有子孙节点，即每一位演员解决了名字分割的问题
        actors = top.find('p',class_='pActor')
        actor= ''
        for act in actors.contents:
            actor = actor + act.string +' '
        #找到影片简介
        intro = top.find('p',class_='pTxt pIntroShow').text

        print("片名：{}\t{}\n{}\t{} \n \n ".format(name,time,actor,intro) )
        # print('这是图片{}'.format(img_url))
        
        #我们来吧图片下载下来：
        with open('./img/'+name+'.png','wb+') as f:
            # f.write(requests.get(img_url).content)   # 此行有问题
            f.write(requests.get("http:"+img_url.split("jpg")[-2]+"jpg").content)

            #说明  aa = '//imgwx1.2345.com/dypcimg/img/9/67/sup203867_223x310.jpg?1562057779'
            # aa.split('jpg')  输出为： ['//imgwx1.2345.com/dypcimg/img/9/67/sup203867_223x310.', '?1562057779']
            # ("http:"+img_url.split("jpg")[-2]+"jpg")  [-2]就是倒数第二个列表切片，
            # 最终组合为  http:////imgwx1.2345.com/dypcimg/img/9/67/sup203867_223x310.jpg
            
            # .content 和 .text 的区别：
            # content用来返回二进制数据，适用于保存二进制数据，例如图像，文件等
            # text适用于显示文本数据，编码根据服务器的响应来显示，也可以自己设置


def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == "__main__":
    main()
