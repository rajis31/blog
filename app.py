from flask import Flask, render_template, redirect,request, json
from flask_paginate import Pagination, get_page_parameter
import pymysql as sql
import os
import json
from models import load_db
import datetime as dt

BASE_DIR      = os.path.dirname(os.path.abspath(__name__))
TEMPLATES_DIR = os.path.join(BASE_DIR,"templates")
CSS_DIR       = os.path.join(os.path.join(BASE_DIR,"static"),"css") 

app = Flask(__name__, static_folder="static", static_url_path="")
app.config.from_json("config.json")

@app.route("/")
def homepage():
    """ Load blog homepage blog listing """

    db = load_db()
    db.connect()
    db.cur.execute("USE articles;")
    db.cur.execute("SELECT * FROM article;")
    articles = [row for row in db.cur.fetchall()]
    return render_template("index.html", articles=articles)


@app.route("/article<int:id>")
def article(id):
    """ Load individual article"""

    db = load_db()
    db.connect()
    db.cur.execute("USE articles;")
    db.cur.execute("SELECT likes FROM article WHERE id = {0};".format(id))
    likes = [i[0] for i in db.cur.fetchall()][0]

    db.cur.execute("SELECT * FROM COMMENTS WHERE article_id = {0} ORDER BY comment_id desc".format(id))
    comments = [comment for comment in db.cur.fetchall()]

    db.cur.execute("SELECT max(id) FROM article;")
    max_id = [i for i in db.cur.fetchall()][0][0]
    db.close()
    return render_template("article{0}.html".format(id), id=id, max_id=max_id, likes=likes, comments=comments)




@app.route("/write",methods=["POST"])
def write():
    """ API endpoint to allow updating and writing of new articles"""

    data    = request.data
    headers = request.headers
    
    data    = data.decode("utf-8")
    
    with open("config.json","r") as f:
        credentials = json.load(f)
        today   = dt.date.today().strftime("%B %d, %Y")
    
    if credentials["article_pass"] == headers["article-pass"]:
        article_name = "article{0}.html".format(headers["article-id"])
        title        = headers["title"]
        if article_name in os.listdir(TEMPLATES_DIR):
            with open(os.path.join(TEMPLATES_DIR,article_name),"w", encoding="utf-8") as f:
                f.writelines(data)
                f.close()

                db = load_db()
                db.connect()
                db.cur.execute("USE articles;")
                db.cur.execute("UPDATE article SET \
                                content = '{0}', date_updated = '{1}' WHERE id = {2};".format(article_name, 
                                today, headers["article-id"]))
                db.close()
        else:
            with open(os.path.join(TEMPLATES_DIR,article_name),"w", encoding="utf-8") as f:
                f.writelines(data)
                f.close()

                db = load_db()
                db.connect()
                db.cur.execute("USE articles;")
                db.cur.execute("INSERT INTO article(title,views,likes,date_posted, \
                                date_updated,content) VALUES \
                                (%s,%s,%s,%s,%s,%s);",(title,0,0,today,today,article_name))
                db.con.commit()
                db.close()


        return "This test successfully"
    else:
        return "Cound not perform article update"


@app.route("/views",methods=["POST"])
def updateViews():
    """ Updates number of Views on a article"""

    data = request.get_json()
    db = load_db()
    db.connect()
    db.cur.execute("USE articles;")
    db.cur.execute("UPDATE article set views={1} where id={0};".format(data['idx']+1,data["views"]+1))
    db.con.commit()
    db.close()
    return ""

@app.route("/likes",methods=["POST"])
def updateLikes():
    """ Updates number of Likes on a article"""

    data = request.get_json()
    db = load_db()
    db.connect()
    db.cur.execute("USE articles;")
    db.cur.execute("UPDATE article set likes={1} where id={0};".format(data['idx'],data["likes"]+1))
    db.con.commit()
    db.close()
    return ""

@app.route("/comment",methods=["POST"])
def addComment():
    """ Updates db with new comment """

    data = request.get_json()
    db = load_db()
    db.connect()
    db.cur.execute("USE articles;")
    db.cur.execute("SELECT IFNULL(max(comment_id),0) FROM comments where article_id=%s;",data["article_id"])
    comment_id = [i[0] for i in db.cur.fetchall()][0]+1
    today   =  dt.datetime.now().strftime("%B %d, %Y %H:%M")

    db.cur.execute("INSERT INTO comments (article_id,comment_id,name, \
                    date_posted,content) VALUES (%s,%s,%s,%s,%s);", \
                    (data["article_id"], comment_id, data["name"], today, data["comment"]))
    db.con.commit()
    db.close()

    return json.dumps({"article_id":data["article_id"], "name": data["name"],  "comment_id":comment_id, \
                       "date_posted":today, "comment": data["comment"]   })


@app.errorhandler(404)
def page_not_found(e):
    """ Handle routes not defined here """
    
    return render_template('404.html'), 404

if __name__=="__main__":
    app.run(debug=True)