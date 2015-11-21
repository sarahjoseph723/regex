from flask import Flask, render_template, request, session, redirect
import json, google, re, requests
from pyquery import PyQuery as pq


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    q = request.args.get('q')
    if q == '':
        return render_template('home')
    else:
        results = []
        for r in google.search(q, num=10, start=0, stop=10):
            results.append(pq(url=r)('body').text())

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
