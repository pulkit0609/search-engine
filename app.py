from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
import os
es = Elasticsearch(os.getenv("ELASTIC_URL"))
INDEX = "skuad_search"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    q = request.form['query']
    body = {
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["title^3", "meta_decription^2", "tags" ,"path"],
                "fuzziness": "AUTO"
            }
        }
    }
    res = es.search(index=INDEX, body=body)
    return render_template('index.html', results=res['hits']['hits'], query=q)

@app.route('/suggest', methods=['GET'])
def suggest():
    prefix = request.args.get('q', '')
    body = {
        "query": {
            "match_phrase_prefix": {
                "title": {
                    "query": prefix
                }
            }
        },
        "_source": ["title"],
        "size": 5
    }
    res = es.search(index=INDEX, body=body)
    return jsonify([hit['_source']['title'] for hit in res['hits']['hits']])


if __name__ == '__main__':
    app.run(debug=True)
