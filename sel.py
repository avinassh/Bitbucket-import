import json

import requests
from requests.auth import HTTPBasicAuth

from templates import sel_script_template
from templates import command_template
from settings import *

def generate_bb_repo_urls():
	def make_rest_call(url):
		auth = HTTPBasicAuth(SRC_AC_USERNAME, SRC_AC_PASSWORD)
		return requests.get(url=url, auth=auth).json()

	seed_url = 'https://bitbucket.org/api/2.0/repositories/' + SRC_AC_USERNAME
	response = make_rest_call(seed_url)
	bb_repo_urls = []

	while('next' in response.keys()):
		for repo in response['values']:
			bb_repo_urls.append(repo['links']['html']['href'])
		response = make_rest_call(response['next'])
	
	return bb_repo_urls

def generate_sel_script(src_repo_urls):
	commands = "".join(map(lambda url: command_template.substitute({
												'bb_username': SRC_AC_USERNAME, 
												'bb_password': SRC_AC_PASSWORD, 
												'repo_url': url,
												'owner_value': IMPORTER_ID
												}), src_repo_urls))

	with open('selenium-script.txt', 'w') as sel_file: 
		sel_file.write(sel_script_template.substitute({
										'bb_username': IMPORTER_BB_USERNAME, 
										'bb_password': IMPORTER_BB_PASSWORD, 
										'commands': commands
										}))

if __name__ == '__main__':
	generate_sel_script(generate_bb_repo_urls())