from bs4 import BeautifulSoup
import scrapy
def to_next_page(response):

    '''

    :param response:
    :return: 下一页的Url,若为None则表示到最后一页了
    '''
    all = response
    soup = BeautifulSoup(all, 'html.parser')
    next = soup.find('a', attrs={"class": "Next"})
    if next == None:
        return None
    else:
        nextUrl = "http://cec.jmu.edu.cn/list.jsp"+next.get("href")
        return nextUrl
def get_all_url(response):
    '''

    :param response:
    :return:本页所有url构成的集合
    '''
    all = response
    soup = BeautifulSoup(all,'html.parser')
    result = soup.find_all('a', attrs={"class": "c124907"})
    allUrl = []
    for i in result:
        allUrl.append("http://cec.jmu.edu.cn/"+i.get("href"))
    return allUrl

def get_title(response):
    '''

    :param response:
    :return:文章标题
    '''
    all = response
    soup = BeautifulSoup(all,'html.parser')
    result = soup.title.text
    return result

def getType(response):
    '''

    :param response:
    :return: 文章的类别
    '''
    all = response
    soup = BeautifulSoup(all,'html.parser')
    result = soup.find_all('span',attrs={"class":"fontstyle116470"})
    return result[-2].text

def getContent(response):
    '''
    :param response:
    :return:
    '''
    all = response
    soup = BeautifulSoup(all, 'html.parser')
    result = soup.find('div', attrs={"class": "v_news_content"})
    content = result.find_all("span")
    cont_string = ""
    if content == []:
        content = result.find_all("p")
    for i in content:
        cont_string = cont_string+i.text
    return cont_string


def getDate(response):
    '''

    :param response:
    :return:
    '''
    all = response
    soup = BeautifulSoup(all, 'html.parser')
    result = soup.find('span', attrs={"class": "timestyle124904"})
    date = result.text
    date.strip()
    return date

