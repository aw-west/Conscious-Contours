# https://aiartists.org/ai-generated-art-tools

filename = './new/1.png'

import requests
r = requests.post(
	'https://api.deepai.org/api/deepdream',
	files={'image': open(filename, 'rb')},
	headers={'api-key': '2f1e180c-bda8-4f5e-adde-940206168037'}
)
print(r.json())
print(r)
