import json

import requests
from requests.auth import HTTPBasicAuth

from templates import sel_script_template
from templates import command_template
from settings import *

def make_rest_call(url):
	auth = HTTPBasicAuth(SRC_BB_USERNAME, SRC_BB_PASSWORD)
	return requests.get(url=url, auth=auth).json()

seed_url = 'https://bitbucket.org/api/2.0/repositories/' + SRC_BB_USERNAME
response = make_rest_call(seed_url)
bb_repo_urls = []

while('next' in response.keys()):
	for repo in response['values']:
		bb_repo_urls.append(repo['links']['html']['href'])
	response = make_rest_call(response['next'])
	break

commands = "".join(map(lambda url: command_template.substitute({
											'bb_username': SRC_BB_USERNAME, 
											'bb_password': SRC_BB_PASSWORD, 
											'repo_url': url,
											'owner_value': IMPORTER_ID
											}), bb_repo_urls))

with open('selenium-scripts.txt', 'w') as sel_file: 
	sel_file.write(sel_script_template.substitute({
												'bb_username': IMPORTER_BB_USERNAME, 
												'bb_password': IMPORTER_BB_PASSWORD, 
												'commands': commands
												}))