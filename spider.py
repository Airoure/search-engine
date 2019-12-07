import requests
import datefinder
import re
from bs4 import BeautifulSoup
from  dbUtil import MySQLCommand
from w3lib.html import remove_comments
import Article
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def getType(type_code):
    if type_code==1044:
        type="学院新闻"
    elif type_code==1043:
        type="院务公开"
    elif type_code==1044:
        type="科研信息"
    elif type_code==1103:
        type="科研工作"
    elif type_code==1010:
        type="学生工作"
    elif type_code==1100:
        type="教学工作"
    elif type_code==1042:
        type="就业工作"
    elif type_code==1067:
        type="会议通知"
    elif type_code==1041:
        type="通知公告"
    elif type_code==1004:
        type="学院风光"
    else:
        type="其他"
    return type
def parsePage(ilt,html):

    soup=BeautifulSoup(html,"html.parser")
    for a in soup.find_all('a',attrs={"class": "c124907"}):
        title=a.get('title')
        href=a.get('href')
        if href.startswith('info/') or href.startswith('content.jsp?urltype=news.NewsContentUrl&wbtreeid='):
            href='http://cec.jmu.edu.cn/'+href
            temp = int(re.search(r'\d+', href).group())
            type = getType(temp)
            html = getHTMLText(href)
            con_html = remove_comments(html)
            con_html =re.sub("<style>.*</style>",'',con_html)
            con_html = re.sub("\n", '', con_html)
            soup2 = BeautifulSoup(con_html, "html.parser")
            s = soup2.find('span', attrs={"class": "timestyle124904"})
            c = soup2.find('div', attrs={"class": "v_news_content"})
            text = s.get_text()
            matches = list(datefinder.find_dates(text))
            time = str(matches[0]).split(" ")[0]
            content = c.get_text()
            article = Article(type,title, href, time, content)
            #th.display()
            ilt.append(article)
def writeDB(ilt):
    db = MySQLCommand()
    db.connectMysql()
    x=1
    for i in ilt:
        db.insertMysql(str(x),i.get_type(),i.get_title(), i.get_href(),i.get_time(),i.get_content())
        #i.display()
        x+=1
    db.closeMysql()


def getMainList(html,mList):
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.findAll('a',attrs={"href":re.compile(r'.*(list.jsp\?urltype=tree.TreeTempUrl&wbtreeid=).*?')}):
        href=a.get('href')
        if not href.startswith("http://cec.jmu.edu.cn/"):
            href="http://cec.jmu.edu.cn/"+href
        mList.append(href)
    for a in soup.findAll('area', attrs={"href": re.compile(r'.*(list.jsp\?urltype=tree.TreeTempUrl&wbtreeid=).*?')}):
        href = a.get('href')
        if not href.startswith("http://cec.jmu.edu.cn/"):
            href = "http://cec.jmu.edu.cn/" + href
        mList.append(href)

def main():
    start_url='http://cec.jmu.edu.cn/index.jsp'

    mainList=[]
    infoList=[]
    start_html=getHTMLText(start_url)
    getMainList(start_html,mainList)
    for l in mainList:
        main_html=getHTMLText(l)
        soup = BeautifulSoup(main_html, "html.parser")
        reg=re.compile(r'共\d+条')
        temp=soup.find(text=reg)
        num=re.search(r'\d+',temp).group()
        total_page=int(num)//10
        for i in range(1,total_page):
            url=l+'&a2p='+str(i)
            html = getHTMLText(url)
            parsePage(infoList, html)
    writeDB(infoList)

main()
