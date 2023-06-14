import requests

url = "http://localhost:9200/ocds/_search"
headers = {
    "Content-Type": "application/json"
}
query = {
	"size": 100000,
    "_source": ["id", "compiledRelease.id", "banderas"],
    "query": {
        "match_all": {}
    }
}
response = requests.post(url, headers=headers, json=query)
data = response.json()
posibles_banderas = set()
def hit_contains(banderas_hit, str_bandera:str):
	for bandera in banderas_hit:
		if(bandera["title"] == str_bandera):
			return True
	return False

for hit in data["hits"]["hits"]:
	# str = hit["_id"]
	if(hit["_source"] and hit["_source"]["banderas"]):
		for bandera in hit["_source"]["banderas"]:
			posibles_banderas.add(bandera["title"])
			# print(bandera)
header = 'id;'
for posible_bandera in posibles_banderas:
	header += posible_bandera + ';'

print(header)

for hit in data["hits"]["hits"]:
	str = hit["_id"]
	if(hit["_source"] and hit["_source"]["banderas"]):
		for posible_bandera in posibles_banderas:
			if(hit_contains(hit["_source"]["banderas"], posible_bandera)):
				str += ";True"
			else:
				str += ";False"
	else:
		for posible_bandera in posibles_banderas:
			str += ";False"
	print(str)
# print([doc.get("id", ""), doc.get("compiledRelease", {}).get("id", "")])

