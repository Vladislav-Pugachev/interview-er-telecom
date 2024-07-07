import http.client
import json

f = open('./test.json')
data = json.load(f)

connection = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
json_data = json.dumps(data['data'])

connection.request('GET', '/json/firts_module/sorted_version/', json_data, headers)

response = connection.getresponse()

print(response.read().decode())

connection.close()
