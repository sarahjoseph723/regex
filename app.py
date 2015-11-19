from flask import Flask, render_template, request, session, redirect
import urllib2, json, google, bs4, re

app = Flask(__name__)

@app.route("/")
def go():
    pass

if __name__=="__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
