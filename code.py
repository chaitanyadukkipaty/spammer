import requests
import os
import random
import string
import json
from data import tags,dep,years

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://139.59.10.44:80/survey'

names = json.loads(open('names.json').read())

for name in names:
	username = name.lower() 
	i = random.randint(0,3);
    department= dep[i];
    year = years[i];
    y = random.randint(0,38);
	tag = tags[:y]
    requests.post(url, allow_redirects=False, data={
		'name': name,
		'department': department,
        'year':year,
        'tags_input':tag
	})