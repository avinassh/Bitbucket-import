import json
from string import Template

import requests
from requests.auth import HTTPBasicAuth

from templates import sel_script_template
from templates import command_template
from settings import BB_USERNAME
from settings import BB_PASSWORD

sel_script = Template(command_template)

# repo_info = { 'repo_url':'myurl'}#, 'repo_name':'myname' }
# print sel_script.substitute(repo_info)

# make call to BB
# see if it has parameter next
# abort if not
# from received data get repo urls.

def make_rest_call(url):
	auth = HTTPBasicAuth(BB_USERNAME, BB_PASSWORD)
	return requests.get(url=url, auth=auth).json()

seed_url = 'https://bitbucket.org/api/2.0/repositories/virtuallabs'
response = make_rest_call(seed_url)
urls = []

while('next' in response.keys()):
	for repo in response['values']:
		urls.append(repo['links']['html']['href'])
	response = make_rest_call(response['next'])

print urls