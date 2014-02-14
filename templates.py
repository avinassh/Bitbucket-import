from string import Template

sel_script_template = Template("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="https://bitbucket.org/account/signin/?next=/repo/import" />
<title>New Test</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">New Test</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>/account/signin/?next=/repo/import</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_username</td>
	<td>$bb_username</td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_password</td>
	<td>$bb_password</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>name=submit</td>
	<td></td>
</tr>
<tr>
	<td>pause</td>
	<td>100</td>
	<td></td>
</tr>

$commands
</tbody></table>
</body>
</html>
""")

command_template = Template("""<tr>
	<td>pause</td>
	<td>1000</td>
	<td></td>
</tr>
<tr>
	<td>open</td>
	<td>https://bitbucket.org/repo/import</td>
	<td></td>
</tr>
<tr>
	<td>pause</td>
	<td>100</td>
	<td></td>
</tr>
<tr>
	<td>open</td>
	<td>https://bitbucket.org/repo/import</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_url</td>
	<td>$repo_url</td>
</tr>
<tr>
	<td>click</td>
	<td>id=id_auth</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_username</td>
	<td>$bb_username</td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_password</td>
	<td>$bb_password</td>
</tr>
<tr>
	<td>select</td>
	<td>id=id_owner</td>
	<td>value=$owner_value</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>xpath=(//button[@type='submit'])[2]</td>
	<td></td>
</tr>""")