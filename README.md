I needed a script to import repositories from other Bitbucket account to my own Bitbucket account. I have some 250 repositories in my account and I wanted them to move under Team (which is same as Organization in Github). Though Bitbucket has APIs, I couldn't find any API to import, instead they provide a HTML form on their site. When I couldn't get my pure [python script][1] to automate and fill the form, I decided to go with Selenium IDE. So following python script generates Selenium IDE script, which I later run on IDE.

This is how this script works:

 - First it makes a REST call to Bitbucket, to find all the repositories
 - The Bitbucket provides a paginated response, the response includes repo URL which is just enough
 - Then I make series of calls to get all repository URLs
 - Once I have got all the URLs, I fill in the selenium script template and write it back to a file 

This script also can be used to import repositories from Github/or any other version control server by importing `generate_sel_script` function. 

  [1]: http://stackoverflow.com/questions/21749403/python-script-using-robobrowser-to-submit-a-form-on-bitbucket-to-import-repo