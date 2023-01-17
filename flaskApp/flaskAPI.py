from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import psycopg2
from flask import render_template, request, Response, json, flash, redirect
app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="datastore",
    user="postgres",
    password="120292"
)
# Create a cursor object
cur = conn.cursor()
# Execute a SELECT statement


# Iterate over the rows and print the data


@app.route("/")
def hello_world():
    return "<p>Hello, Welcoeme to Social Media APP</p>"


@app.route("/getMessages", methods=["GET"])
def getMessage():

    cur.execute("""select * from messages order by "msgid" DESC""")
    rows = cur.fetchall()
    msg = []
    for row in rows:
        msg.append(row)
    rdata = {
        "status": msg
    }
    return Response(json.dumps(rdata), mimetype="application/json")


@app.route("/postMessage", methods=["POST"])
def postMessage():
    # if (request.is_json()):
    #     msg = request.get_json()

    msgs = request.get_json()

    cur.execute("insert into messages (message) values (%s)",
                (msgs["message"],))

    conn.commit()
    rdata = {
        "status": "Successful"
    }
    return Response(json.dumps(rdata), mimetype="application/json")


@app.route("/likeMessage/<msgId>", methods=["PUT"])
def likeMessage(msgId):


    cur.execute(
        """ select lcount from likes where "messageid"=%s; """, (int(msgId),))
    lcount = cur.fetchone()

    lcount = int(lcount[0])+1
    cur.execute(""" update likes set lcount = %s where  "messageid"=%s""",
                (lcount, int(msgId),))
    conn.commit()
    rdata = {
        "status": "liked"
    }
    return Response(json.dumps(rdata), mimetype="application/json")


@app.route("/dislikeMessage/<msgId>", methods=["PUT"])
def dislikeMessage(msgId):

    

    cur.execute(
        """ select lcount from likes where "messageid"=%s """, (msgId,))
    lcount = cur.fetchone()
    lcount = int(lcount[0])-1
    if (lcount<0):
        lcount = 0
    cur.execute(""" update likes set lcount = %s where  "messageid"=%s""",
                (lcount, int(msgId),))
    conn.commit()
    rdata = {
        "status": "disliked"
    }
    return Response(json.dumps(rdata), mimetype="application/json")


@app.route("/viewLikes", methods=["GET"])
def viewMessage():

    cur.execute(
        """ select message,lcount from messages,likes where "msgid"="messageid" ; """)
    rows = cur.fetchall()
    msg = []
    for row in rows:
        msg.append(row)
    conn.commit()
    rdata = {
        "status": msg
    }
    return Response(json.dumps(rdata), mimetype="application/json")
