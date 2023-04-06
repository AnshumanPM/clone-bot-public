from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Bot Running, Made By <a href='https://telegram.me/AnshumanPM_2006'>𝑨𝒏𝒔𝒉𝒖𝒎𝒂𝒏𝑷𝑴 〄</a></h1>"
