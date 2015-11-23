from flask import Flask, render_template, request, session, redirect
import json, google, re, requests, bs4, urllib2
from pyquery import PyQuery as pq


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    q = request.args.get('q')
    #if no query
    if q == '':
        return render_template('home.html')
    #there is a query
    else:
        results = []
        for r in google.search(q, num=10, start=0, stop=10):
            results.append(pq(url=r)('body').text())
            #results.append(r)
        
            print results

        return 'howdy'


# # Parses Query
# def parse(query):
#
#
# # Find answer in text
# def find(type, value, text):




if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
