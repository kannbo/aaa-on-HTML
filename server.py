from main import aaa
from bottle import run,route,get,post,request
koukai=[]
@get("/")
def getget():
    return """<form action="/" method="post"><textarea name="area"></textarea><input value="変更" type="submit" /></form>"""
@post("/")
def postpost():
    global koukai
    print(aaa(request.forms.area))
    koukai.append(aaa(request.forms.area))
    return aaa(request.forms.area)
@route("/page=<name>")
def aaaaw(name):
    global koukai
    return koukai[int(name)]
run(port="8888",host="localhost")
