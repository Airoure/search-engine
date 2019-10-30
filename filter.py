# encoding=utf-8
# 导入爬虫包
from selenium import webdriver
import re
import os
import requests
# 打开编码方式utf-8打开
 
if __name__ == '__main__':
   # fR = open('D:\\test.txt','r',encoding = 'utf-8')
 
    # 模拟浏览器，使用谷歌浏览器，将chromedriver.exe复制到谷歌浏览器的文件夹内
    chromedriver = r"C:\\Users\\zhaofahu\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    # 设置浏览器
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)

    # 要爬取的网页
    neirongs = []  # 网页内容
    response = []  # 网页数据
    urls = []
    titles = []
    writefile = open("docs.txt", 'w', encoding='UTF-8')
    url = 'http://www.jmu.edu.cn/'
    # 第一页
    browser.get(url)
    response.append(browser.page_source)
 
    # 用正则表达式来删选数据
    reg = r'href="(^http://www.jmu.edu.cn/.*?)"'
    # 从数据里爬取data
    for i in range(len(response)):
        urls = re.findall(reg, response[i])
 