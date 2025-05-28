import json

with open("kibana_tags.json", "r") as f:
    kibana_data = json.load(f)

buckets = kibana_data["aggregations"]["top_tags"]["buckets"]
high_freq_tags = {bucket["key"] for bucket in buckets if bucket["doc_count"] >= 650}

print("high_freq_tags = {")
for tag in sorted(high_freq_tags):
    print(f'    "{tag}",')
print("}")
