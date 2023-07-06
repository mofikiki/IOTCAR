from flask import Flask,request, render_template
import socket
import pandas as pd
global state1
state1="S"
app = Flask(__name__)
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

# @app.route("/")
# def home() :
#     print(state1)
#     return render_template('control.html')
@app.route("/getstate", methods=['GET'])
def getstate():
    global state1
    result = state1
    return (result)


@app.route("/move")
def move() :
    global state1
    state1= request.args.get("new_state1")
    print("Successful")
    




if __name__=="__main__":
    app.run(host =str(ipaddr),port = 80, debug = False,threaded = True)

