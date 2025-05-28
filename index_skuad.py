from elasticsearch import Elasticsearch, helpers
import json

es = Elasticsearch("http://localhost:9200")
INDEX = "skuad_search"

if not es.indices.exists(index=INDEX):
    es.indices.create(index=INDEX)


with open("skuad_meta_cleaned.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

actions = []
for i, doc in enumerate(docs, start=1):
    path_parts = doc.get("path", "").split(" > ")
    tags_list = [tag.strip() for tag in doc["tags"] if tag.strip()]


    actions.append({
        "_index": INDEX,
        "_id":    i,
        "_source": {
            "title":      doc["title"],
            "url":        doc["url"],
            "path":       doc["path"],
            "path_parts": path_parts,
            "tags":       tags_list,
            "meta_description": doc["meta_description"],
            "suggest": {
                "input": path_parts + doc["title"].split()
            }
        }
    })


helpers.bulk(es, actions)
print(f"✅ Indexed {len(actions)} documents into '{INDEX}'.")
