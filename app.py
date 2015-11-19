from flask import Flask, render_template, request, session, redirect
import json, google, re
from pyquery import PyQuery as pq

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    q = request.args.get('user')
    if q != '':
			print 'yo'
    else: 
			results = []
			i = 0
			print google.search(q, num=10, start=0, stop=10)
			#for r in google.search(q, num=10, start=0, stop=10):
			#	d = pq(url=r)
			#	results[i] = d.html()
			#	i+=1

			print results

			 



if __name__=="__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
