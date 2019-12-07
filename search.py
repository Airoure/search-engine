from  dbUtil import MySQLCommand
from flask import *
from datetime import timedelta
from page_utils import Pagination

search=Flask(__name__)
search.config['SEND_FILE_MAX_AGE_DEFAULT']= timedelta(seconds=1)

@search.route("/")
def index():
    return render_template('index.html')


@search.route("/result",methods = ['POST', 'GET'])
def result():
    wd=request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list=db.queryMysql(wd,'')  # 查询数据
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth=len(list)
    return render_template("result.html", list=index_list, html=html,lenth=lenth)

@search.route("/1044")
def index_1044():
    wd = request.args.get('wd')
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '学院新闻')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1043")
def index_1043():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '院务公开')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1103")
def index_1103():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '科研信息')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1010")
def index_1010():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '科研工作')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1112")
def index_1112():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '学生工作')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1100")
def index_1100():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '教学工作')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1042")
def index_1042():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '就业工作')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1067")
def index_1067():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '会议通知')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1041")
def index_1041():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '通知公告')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.route("/1004")
def index_1004():
    wd = request.values.get("wd")
    db = MySQLCommand()
    db.connectMysql()
    list = db.queryMysql(wd, '学院风光')
    pager_obj = Pagination(request.args.get("page", 1), len(list), request.path, request.args, per_page_count=10)
    index_list = list[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    lenth = len(list)
    return render_template("result.html", list=index_list, html=html, lenth=lenth)

@search.template_test('current_link')
def is_current_link(link):
    return link == request.path
if __name__ == '__main__':
    search.run(port=7000,debug=True)
