import pymysql as sql
import json
import datetime as dt 


class load_db:
    def __init__(self):
        with open("config.json") as f:
            self.credentials = json.load(f)

    def connect(self):
        username = self.credentials["username"]
        password = self.credentials["password"]
        self.con = sql.connect("localhost", username, password)
        self.cur = self.con.cursor()

    def createDB(self, dbName):
        self.cur.execute("SHOW DATABASES;")
        res = [db[0] for db in self.cur.fetchall()]
        if dbName not in res:
            self.cur.execute("CREATE DATABASE {0};".format(dbName))
        else:
            self.cur.execute("USE {0};".format(dbName))

    def createTable(self, tableName, meta):
        create_table = "CREATE TABLE IF NOT EXISTS {0} (".format(tableName)
        field_names = list(meta.keys())

        for field in field_names:
            if field != field_names[-1]:
                create_table += "{0} {1},".format(field, meta[field])
            else:
                create_table += "{0} {1});".format(field, meta[field])

        print(create_table)

        try:
            self.cur.execute(create_table)
        except:
            print("ERROR IN CREATE TABLE STATEMENT")

    def deleteTable(self, table):
        try:
            self.cur.execute("DROP TABLE {0};".format(table))
        except:
            print("Table does not exist")

    def insertRecord(self, table, data):
        columns =[x.replace("'",'')  for x in  list(data.keys())]

     
        self.cur.execute(insert)
        self.con.commit()

    def close(self):
        self.cur.close()
        self.con.close()


con = load_db()

if __name__ == "__main__":
    con.connect()
    con.createDB("articles")
    con.deleteTable("article")
    con.createTable("article", {"id": "int primary key auto_increment", "title": "varchar(255)",
                                "views": "bigint", "likes": "bigint", "date_posted": "varchar(255)",
                                "date_updated": "varchar(255)", "content": "mediumtext"})
   
    con.createTable("comments",{"article_id":"int","comment_id":"int","name":"varchar(50)",
                                "date_posted":"varchar(100)","content":"text"})

    # import os 
    # PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
    # HTML_DIR   = os.path.join(PARENT_DIR,"templates")

    
    # with open(os.path.join(HTML_DIR,"article.html"),encoding="UTF-8") as f:
    #     content = "".join(f.readlines())
    #     print(type(content))
    #     today   = dt.date.today().strftime("%B %d, %Y")
    #     con.cur.execute("""
    #         INSERT INTO ARTICLE (title,views,likes,date_posted,date_updated,content) VALUES 
    #             ('%s','%s','%s','%s','%s','%s');
    #     """%("How to install Flask",0,0,today,today,"article.html"))

    #     con.con.commit()
        
    con.close()
