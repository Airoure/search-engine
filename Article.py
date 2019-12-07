
class Article():
    def __init__(self,type,title,href,time,content):
        self.type = type
        self.title=title
        self.href=href
        self.content=content
        self.time=time

    def display(self):
        print("类型："+self.type)
        print("标题："+self.title)
        print("链接："+self.href)
        print("时间：" + self.time)
        print("内容：" + self.content)
    def get_type(self):
        return self.type
    def get_href(self):
        return self.href
    def get_title(self):
        return self.title
    def get_content(self):
        return self.content
    def get_time(self):
        return self.time