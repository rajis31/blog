from flask import Flask
import pymysql as sql

app = Flask(__name__)
app.config.from_json("config.json")







if __name__=="__main__":
    app.run()