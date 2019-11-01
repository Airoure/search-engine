from flask import Flask, render_template, request
from realITspider import elasticSearchUtils
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/result",methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        searchWord=request.values.get("searchWord")
        res = elasticSearchUtils.default_search("itartical",searchWord)
        list = []
        for i in res:
            item = []
            item.append(i.get_title())
            item.append(i.get_content())
            item.append(i.get_href())
            item.append(i.get_time())
            item.append(i.get_type())
            list.append(item)
        if list == []:
            render_template("index.html")
        else:
            return render_template("result.html",result=list)
if __name__ == '__main__':
    app.run(debug=True)