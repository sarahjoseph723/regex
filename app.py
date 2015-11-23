from flask import Flask, render_template, request, session, redirect
import json, google, re, requests
from pyquery import PyQuery as pq
import analyze, time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    who = False
    when = False
    q = request.args.get('q');
    #if no query
    if q == None:
        return render_template('home.html')
    #there is a query
    else:
        #should probably check for "Who" and "When" also                      
        words = q.split()
        #check what kind of query it is
        if "who" in words:
            who = True
        elif "when" in words:
            when = True
        results = []
        time.sleep(0.01)
        for r in google.search(q, num=10, start=0, stop=1):
            results.append(pq(url=r)('body').text())
            #print results
        returned = []
        if who:
            answer=analyze.getMode(analyze.who(results))
            return render_template('results.html',answer = answer)
        elif when:
            answer=analyze.getMode(analyze.when(results))
            return render_template('results.html',answer = answer)
        else:
            return render_template('home.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
