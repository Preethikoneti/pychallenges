# -*- coding: utf-8 -*-
''' Box to Google Drive Tool
	 Author: Kevin Beattie
	   Date: 04/19/2017
Description: An OAuth2 utility to read sharing permissions of files and folders on Box and apply them to their counterpart on 
			 Google Drive after migrated.
  Doc Links: 1) Box API Reference - https://docs.box.com/reference#files
  			 2) Box API Error Messages & Solutions - https://developer.box.com/v2.0/docs/detailed-error-messages
  			 3) FAQ: Box Platform and APIs - https://community.box.com/t5/Developer-Forum/FAQ-Box-Platform-and-APIs/m-p/14768#U14768
	  Usage: (pending)
'''    
import collections, json, requests, jwt, uuid, datetime, urllib, os, sys, getopt, argparse, csv, collections, re
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa, rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key
# from boxsdk import Client
from validate_email import validate_email
from myTests import boxapitests
from bcolors import *

with open('secrets.json') as secrets_file:
	data = json.load(secrets_file)
	key_password = data['password']
	client_secret = data['client_secret']

# Variables
global_groups = []
global_local_group = {}
# key = load_pem_private_key(open('private_key.pem').read(), password=key_password, backend=default_backend())
api_url = "https://api.box.com/oauth2/token"
usr_url = "https://api.box.com/2.0/users/"
group_url = "https://api.box.com/2.0/groups"
folder_url = "https://api.box.com/2.0/folders/"
file_url = "https://api.box.com/2.0/files/"
# client_id = "csxwusv75ku40rfhpj2r2lgdbzdgt8qz" # This is also known as the API Key
# client_secret = client_secret
key = load_pem_private_key(open('private_key.pem').read(), password="dc1bd85ec15d6d2f036c61ededec92e5", backend=default_backend())
client_id = "csxwusv75ku40rfhpj2r2lgdbzdgt8qz"
client_secret = "i4GgjZusu1tqVlEZwhkcpY5M7TBtj8Ox"
#aud = "https://api.box.com/oauth2/token"
tenant_enterprise_id = "58091"
iat = int(((datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).total_seconds())+0)
iat_time = datetime.datetime.fromtimestamp(iat).strftime('%c')
exp = int(((datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).total_seconds())+60)
exp_time = datetime.datetime.fromtimestamp(exp).strftime('%c')
# Generates a random hex for the jti
jti = (uuid.uuid4()).hex
# if (debug):
	### BOLD
# heading = """
####################################################################'
"Application Client ID (issuer): """ + str(client_id) + """
"JWT Audience: """ + str(api_url) + """
"JWT Issued at Time (UNIX Epoch): """ + str(iat) + """
"JWT Issued at Time: """ + str(iat_time) + """
"Expiry Time for JWT (UNIX Epoch): """ + str(exp) + """
"Expiry Time for JWT: """ + str(exp_time) + """
"jti unique identifier: """ + str(jti) + """
'#####################################################################"""
# bcolors.color('BOLD',str(heading))
box_sub_type = "enterprise"
enterprise_assertion = jwt.encode({"iss": client_id,"sub": tenant_enterprise_id,"box_sub_type": box_sub_type, "aud": api_url,"jti": jti,"exp": exp,}, key, algorithm='RS256', headers={"alg": "RS256","typ": "JWT"})
auth_data = [
  ('grant_type', 'urn:ietf:params:oauth:grant-type:jwt-bearer'),
  ('client_id', client_id),
  ('client_secret', client_secret),
  ('assertion', enterprise_assertion),
]
# if (debug):
# 	msgStr = "(DEBUG) Header JSON Data: " + str(auth_data)
# 	bcolors.color('HEADER',msgStr)

def stripNonAlphaNum(text):
    return re.compile(r'\W+', re.UNICODE).split(text)

def convert(data):
	# print "Hi I'm converting data here!"

	return data

def authorize(data):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: authorize ")
		bcolors.color('HEADER',"Data Received: " + str(data))
	r = requests.post(api_url, data=data)
	try:
		load = r.json()
		load.has_key('access_token')
		# YAY! We has a token!
		token = load['access_token']
		if (debug):
			bcolors.color('HEADER',"(DEBUG) JSON Data Returned from API: " + str(r.json()) + "\n Access Token: " + str(token))
		return token
	except ValueError, e:
		return False

def appuser_create(access_token):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: appuser_create")
		bcolors.color('HEADER'," \nData Received: \n access_token: " + str(access_token))

	def do_curl():
		# EXAMPLE: curl https://api.box.com/2.0/users -H "Authorization: Bearer Th5KytmEJuyCT4aCGOY2oqq33vJ9SdT3" -d '{"name": "Ned Stark", "is_platform_access_only": true}' -X POST
		# This function exists for testing only.
		token = "Bearer " + str(access_token)
		headers = "Authorization: " +str(token)
		data = '{"name": "Ned Stark", "is_platform_access_only": true}'
		curl_c = "curl " + str(usr_url) + " -H \""+ str(headers) +"\" -d " + "\'"+ str(data) +"\'" + " -X POST"
		if (debug):
			print " CURL Command: " + str(curl_c)
		r = subprocess.check_output(curl_c, shell=True)
		if (debug):
			print " API Reponse: " + str(r)
			load = json.loads(r)
			print "  JSON (str) Data: " + str(type(r)) + str(r)
			print " JSON (ditc) Data: " + str(type(r)) + str(r)
			# print " User ID: " + str(r['id'])
		# load = r.json()
		# return load['id']

	def do_requests():
		token = "Bearer "+str(access_token)
		# headers = "{\'Authorization\': \'"+headers+"\',}"
		headers = {
		  #'Fake-Value': '42',
		  'Authorization': token,
		}
		data = '{"name": "Ned Stark", "is_platform_access_only": true}'
		if (debug):
			bcolors.color('HEADER',"Headers:" + str(type(headers)) +" "+str(headers)+"\nData:" + str(type(data)) +" "+str(data))
		r = requests.post(usr_url, headers=headers, data=data)
		if (debug):
			print " API Reponse: " + str(r)
			load = r.json()
			print " JSON Data: " + str(load)
			print " User ID: " + str(load['id'])
		load = r.json()
		return load['id']

	# do_curl() # Don't use this! It was added for testing.
	user_id = do_requests()
	return user_id
	if (debug):
		bcolors.color('HEADER',"(DEBUG) End of Funtion")

def get_user_token(user_id):
	box_sub_type = "user"
	tenant_enterprise_id = user_id
	jti = (uuid.uuid4()).hex
	enterprise_assertion = jwt.encode({"iss": client_id,"sub": tenant_enterprise_id,"box_sub_type": box_sub_type, "aud": api_url,"jti": jti,"exp": exp,}, key, algorithm='RS256', headers={"alg": "RS256","typ": "JWT"})
	data = [
	  ('grant_type', 'urn:ietf:params:oauth:grant-type:jwt-bearer'),
	  ('client_id', client_id),
	  ('client_secret', client_secret),
	  ('assertion', enterprise_assertion),
	]	
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: get_user_token ")
		bcolors.color('HEADER',"Data Received: \n user_id: " + str(user_id) + "\nBox Sub Type: " + str(box_sub_type))
		bcolors.color('HEADER',"Box App User: " + str(tenant_enterprise_id) + "\nEnterprise Assertion: " + str(enterprise_assertion))
	try:
		token = authorize(data)
		if(token):
			return token
		else:
			print bcolors('FAIL',"Failed to get a token for user ",user_id,": ",str(sub_values))
	except ValueError, e:
		return False

def get_user_id(access_token, user_email):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: get_user_id ")
		bcolors.color('HEADER',"Data Received: \n access_token: " + str(access_token) + "\n user_email: " + str(user_email))
	user_email = user_email.replace('@', '%40')
	api_url = usr_url + "?filter_term="+ str(user_email) + "&fields=id"
	token = "Bearer " + str(access_token)
	headers = {
	    'Authorization': token,
	}
	r = requests.get(api_url, headers=headers)
	try:
		load = r.json()
		if load.has_key('entries'):
			# Yay! So far so good!
			sub_values = load['entries']
			for value in sub_values:
				if 'id' in value:
					# Yay! We has good data!
					return value['id']
				else:
					print bcolors('FAIL',"Failed to find \'id\' value in the data: " + str(sub_values))
		if (debug):		
			bcolors.color('HEADER',"API URL: " + str(api_url) + "\nAPI Response:" + str(r) + " JSON Data Received: " + str(load) + " User ID: " + str(user_id))
	except ValueError, e:
		return False

def get_user_info(access_token, user_id):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: get_user_info ")
		bcolors.color('HEADER',"Data Received: \n user_id: " + str(user_id) + "\n access_token: " + str(access_token))
	api_url = usr_url + str(user_id)
	token = "Bearer " + str(access_token)
	headers = {
	    'Authorization': token,
	}
	r = requests.get(api_url, headers=headers)
	try:
		load = r.json()
		if load.has_key('id'):
			# YAY! We has good data!
			if (debug):
				bcolors.color('HEADER',"API URL: " + str(api_url) + "\nAPI Response:" + str(r) + "\n JSON Data Received: " + str(load))
		return load
	except ValueError, e:
		return False

def get_folder_contents(user_token, folder_id):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: get_folder_contents ")
		bcolors.color('HEADER',"Data Received: \n user_token: " + str(user_token) + "\n folder_id: " + str(folder_id))
	api_url = folder_url + str(folder_id)
	token = "Bearer " + str(user_token)
	headers = {
	    'Authorization': token,
	}
	r = requests.get(api_url, headers=headers)
	if '200' in str(r):
		# c = 1
		load = r.json()
		load = convert(load)
	# 	if not (debug):
	# 		if not load['entries']:
	# 			print " (empty group)"
	# 		else:
	# 			for items in load['entries']:
	# 				print " " + str(c) + ") " + (items['name']) + ", "+ (items['type']) + ", " + (items['user']['id'])
	# 				c += 1
	# 	if (debug):
	# 		bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))
	# 	return True
	# else:
	# 	bcolors.color('FAIL',"API Response: " + str(r))
	# 	load = r.json()
		if (debug):
			bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))
		return load
	else:
		bcolors.color('FAIL',"API Response: " + str(r))

def get_box_groups(token):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: get_box_groups ")
		bcolors.color('HEADER',"Data Received: token: " + str(token))
	api_url = group_url
	token = "Bearer " + str(token)
	headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
	    'Authorization': token,
	}
	if (debug):
		bcolors.color('HEADER',"API URL: " + str(api_url) + "\nHeaders: " + str(headers))
	r = requests.get(api_url, headers=headers)
	if '200' in str(r):
		load = r.json()
		if (debug):
			bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))
		return convert(load)
	else:
		bcolors.color('FAIL',"API Response: " + str(r))

def get_group_members(token, group_id, group_name="none"):
	if (debug):
		bcolors.color('WARNING',"(DEBUG) Running Function: get_group_members ")
		bcolors.color('HEADER',"Data Received: token: " + str(token) + "\n group_id: " + str(group_id))
	api_url = str(group_url) + "/"+str(group_id)+"/memberships"
	token = "Bearer " + str(token)
	headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
	    'Authorization': token,
	}
	if (debug):
		bcolors.color('HEADER',"API URL: " + str(api_url) + "\nHeaders: " + str(headers))
	r = requests.get(api_url, headers=headers)
	if '200' in str(r):
		c = 1
		load = r.json()
		if not debug:
			print "Group \'" + str(group_name) + "\' with ID "+str(group_id)+" contains the following members:" 
		if not (debug):
			if not load['entries']:
				print " (empty group)"
			else:
				for items in load['entries']:
					print " " + str(c) + ") " + (items['user']['name']) + ", "+ (items['user']['login']) + ", " + (items['user']['id'])
					c += 1
		if (debug):
			bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))		
		return True
	else:
		bcolors.color('FAIL',"API Response: " + str(r))

def get_group_members_recursive(token, group_data):
	try:
		if group_data.has_key('entries'):
			# Yay! So far so good!
			print "Please wait while we retreive group information from box.com..."
			sub_values = group_data['entries']
			groups = convert(sub_values)
			for group in groups:
				# print "Group \'" + str(group["name"]) + "\' with ID "+str(group["id"])+" contains the following members:" 
				members = get_group_members(token, group["id"], group["name"])
	except ValueError, e:
		return False

def do_getAllGroups():
	token = authorize(auth_data)
	all_groups = get_box_groups(token)
	return all_groups

def do_getGroup(name):
	namelc = str(name).lower()
	all_box_groups = do_getAllGroups()
	matches = {}
	c = 1
	# print str(type(group_name)), str(group_name)
	# print str(type(all_box_groups)), str(all_box_groups)
	try:
		if all_box_groups.has_key('entries'):
			# Yay! So far so good!
			print "Please wait while we search for \""+ str(name) +"\" in Groups on box.com..."
			sub_values = all_box_groups['entries']
			groups = convert(sub_values)
			for group in groups:
				if namelc in group["name"].lower():					
					matches[(group["name"])] = group["id"]
			if len(matches) == 0:
				print "Sorry, no groups with \""+ str(name) +"\" in the name was found."
			else:
				print "Result: "+str(len(matches))+" groups matched your query."
				for key,val in matches.items():
					print " " + str(c) + ") " + "{}, has ID {}".format(key, val)
					c += 1
	except ValueError, e:
		return False

### NEW FUNCTIONS ###
# NEW: GET SHARE LINK
def do_getShareLink(fileid):
	# In order to lookup files, we need the id of the user, then a user token
	print "Received File ID: " + str(fileid)
	access_token = authorize(auth_data) # Get an auth token
	userid = get_user_id(access_token, "boxadmin@yelp.com") # Get the user id
	token = get_user_token(userid) # Get the user token
	if not token:
		# No token
		pass
	else:
		# YAY token
		if (debug):
			bcolors.color('WARNING',"(DEBUG) Running Function: do_getSharedFile ")
			bcolors.color('HEADER',"Data Received: \n token: " + str(token) + "\n fileid: " + str(fileid))
		api_url = file_url + str(fileid) + str("?fields=shared_link")
		token = "Bearer " + str(token)
		headers = {
			'Authorization': token,
		}
		r = requests.get(api_url, headers=headers)
		if '200' in str(r):
			# c = 1
			load = r.json()
			load = convert(load)
			if (debug):
				bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))
			print load
		else:
			bcolors.color('FAIL',"API Response: " + str(r))

# NEW: Get Info for File for Folder
def do_getFileInfo(fileid):
	# fileid = stripNonAlphaNum(fileid)
	# In order to lookup files, we need the id of the user, then a user token
	access_token = authorize(auth_data) # Get an auth token
	userid = get_user_id(access_token, "boxadmin@yelp.com") # Get the user id
	token = get_user_token(userid) # Get the user token
	path = ""
	if not token:
		# No token
		pass
	else:
		# YAY token
		if (debug):
			bcolors.color('WARNING',"(DEBUG) Running Function: do_getSharedFile ")
			bcolors.color('HEADER',"Data Received: \n token: " + str(token) + "\n fileid: " + str(fileid))
		api_url = file_url + str(fileid)
		token = "Bearer " + str(token)
		headers = {
			'Authorization': token,
		}
		r = requests.get(api_url, headers=headers)
		if '200' in str(r): # If return code 200, we load the data into JSON format
			# c = 1
			load = r.json()
			load = convert(load)
			if (debug):
				bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))

			file_name =  load['name']
			share_ink = load['shared_link']
			path_collection = load['path_collection']['entries']
			for folder in path_collection:
				path+=folder['name']+"\\"
			# print "<File ID>,<File Path>,<File Name>,<Share Link>"
			print fileid,"`",path.encode('ascii', 'ignore')+file_name.encode('ascii', 'ignore')
			# result = str(fileid)+","+str(path)+"."+str(file_name)+","+str(share_ink)
			# return result
		else:
			bcolors.color('FAIL',"API Response: " + str(r))

# NEW: Get File Info
def do_getFileInfo(fileid):
	# fileid = stripNonAlphaNum(fileid)
	# In order to lookup files, we need the id of the user, then a user token
	access_token = authorize(auth_data) # Get an auth token
	userid = get_user_id(access_token, "boxadmin@yelp.com") # Get the user id
	token = get_user_token(userid) # Get the user token
	path = ""
	if not token:
		# No token
		pass
	else:
		# YAY token
		if (debug):
			bcolors.color('WARNING',"(DEBUG) Running Function: do_getSharedFile ")
			bcolors.color('HEADER',"Data Received: \n token: " + str(token) + "\n fileid: " + str(fileid))
		api_url = file_url + str(fileid)
		# api_url = folder_url + str(fileid)
		token = "Bearer " + str(token)
		headers = {
			'Authorization': token,
		}
		r = requests.get(api_url, headers=headers)
		if '200' in str(r): # If return code 200, we load the data into JSON format
			# c = 1
			load = r.json()
			load = convert(load)
			if (debug):
				bcolors.color('HEADER',"API Response:" + str(r) + "\nJSON Data Received: " + str(load))

			file_name =  load['name']
			share_ink = load['shared_link']
			path_collection = load['path_collection']['entries']
			for folder in path_collection:
				path+=folder['name']+"\\"
			# print "<File ID>,<File Path>,<File Name>,<Share Link>"
			print fileid,"`",path.encode('ascii', 'ignore')+file_name.encode('ascii', 'ignore')
			# result = str(fileid)+","+str(path)+"."+str(file_name)+","+str(share_ink)
			# return result
		else:
			bcolors.color('FAIL',"API Response: " + str(r))

# NEW: Batch Get File Info
def do_batch_FileInfo(inputFile):
	report = ""
	print "Opening file "+inputFile+" ..."
	try:
		print "<File ID>,<File Path>,<File Name>,<Share Link>"
		with open(inputFile) as f:
			lines = list(line for line in (l.strip() for l in f) if line)				
			for fileid in lines:
				print fileid
				do_getFileInfo(fileid)
			# print fileid
			# result = do_getFileInfo(fileid)
			# report+=report+result
				# print result
			# return True
	# except:
	# 	print "Error: Could not read file "+inputFile
	finally:
		# for line in report:
		# 	print line
		print ":-)"

	# out_file = str("/Users/kbeattie/Documents/Dev/Python/boxAPItool/")+str(uuid.uuid4())
	# # Open CSV for Writing and Create if Not Exist
	# try:
	# 	f = open(out_file, 'r')
	# except:
	# 	f = open(out_file, 'w')
	# with open(out_file, 'rb') as f:
	# 	data = list(csv.reader(f))
	# f = open(out_file,'w')
	# f.write(str("Some Data"))
	# f.close()

def do_reportAllGroupMembers():
	token = authorize(auth_data)
	all_groups = get_box_groups(token)
	get_group_members_recursive(token, all_groups)

def do_user_lookup(user):
	auth_token = authorize(auth_data)
	print "Getting token for " + str(user)
	user_id = get_user_id(auth_token,user)
	user_token = get_user_token(user_id)
	if user_token:
		msg_str = "Acquired access token for \'" + str(user) + "\' : " + str(user_token)
		bcolors.color('OKGREEN',"SUCCESS: " + str(msg_str))
		return user_token
		# folder_contents = get_folder_contents(user_token,0)
		# print str(folder_contents)
	else:
		msg_str = "Unable to acquire token for \'" + str(user) + "\'"
		bcolors.color('FAIL',"ERROR: " + str(msg_str))
		return false

def is_valid_email(input_string):
	result = validate_email(input_string)
	if "yelp.com" not in input_string:
		msg_str = "Email address \'" + str(input_string) + "\' does not belong to Yelp.com"
		bcolors.color('FAIL',"ERROR: " + str(msg_str))
		usage()
		return False
	else:
		if (result):
			return True
		else:
			msg_str = "Malformed email address \'" + str(input_string) + "\'"
			bcolors.color('FAIL',"ERROR: " + str(msg_str))
			usage()
			return False

def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x

def is_error(err):
	bcolors.color('FAIL',"ERROR: " + str(err))
	usage()
	sys.exit(2)

def usage():
	print '''\nYelp's Box API Tool v0.0.0.1
Authored by Kevin Beattie <kbeattie@yelp.com>
Requires Python 2.7.6 64-bit final'''
	#parser.print_help()
# Usage: app.py [OPTIONS]

# Examples:
#   python app.py -h 	Display this help file
#   python app.py -gm, --groupmembers 	Generage a report of all groups in Box and their members
#   python app.py -g, --group <group name>  Generate a report on a group 
#   python app.py -u, --user <user@yelp.com> 	Generate a report on a user
#   python app.py -d, --debug 	Runs tests and displays useful debugging information
#	'''

def do_tests():
	# Variables
	user_email = "kbeattie@yelp.com"	
	admin_email = "boxadmin@yelp.com"	
	admin_id = '11974240' # Box Admin ID = 11974240
	group_id = '225187' # Accounting Group
	group_name = 'Accounting' # Accounting
	# Run Tests Below
	tests = boxapitests()
	tests.test_isAPIavailable(api_url)
	token = authorize(auth_data)
	tests.test_isTokenReceived(token)
	user_data = get_user_info(token, admin_id)
	tests.test_isBoxAdmin(user_data)
	admin_id = get_user_id(token, admin_email)
	tests.test_getUserID(admin_id)
	user_id = get_user_id(token, user_email)
	user_token = get_user_token(user_id)
	tests.test_isUserToken(user_token)
	group_data = get_box_groups(token)
	tests.test_getBoxGroups(group_data)
	group_members = get_group_members(token, group_id, group_name)
	tests.test_getgrouptmembers(group_members)
	folder_contents = get_folder_contents(user_token,0)
	tests.test_getFolderContents(folder_contents)

def main(argv):
	try:
		global debug
		debug = False # Debugging disabled by default, use flag --debug to turn on debugging
		parser = argparse.ArgumentParser(description="Yelp's Box API Tool v0.0.0.1, Authored by Kevin Beattie <kbeattie@yelp.com>, Requires Python 2.7.6 64-bit final")
		parser.add_argument("-gm", "--groupmembers", dest="groupmembers", action="store_true", help="Generage a report of all groups in Box and their members")
		parser.add_argument("-g", "--group", action="store", dest="group", type=str, help="Generate a report on a group")
		# subparsers = parser.add_subparsers(help="Report on user usage")
		parser.add_argument("-u", "--user", action="store", dest="user", type=str, help="Generate a report on a user")
		# parser.add_argument('-f', '--file', action="store", dest="file", type=str, help="An ID# for a file")
		parser.add_argument('--fileid', action="store", dest="fileid", type=int, help="An ID# for a file")
		# parser.add_argument('-b', '--batch', action="store", dest="batch", type=str, help='Input file, in multi-line text format')
		parser.add_argument("-i", "--input", dest="input", required=False, type=extant_file, help="input file with two matrices", metavar="FILE")
		parser.add_argument("-d", "--debug", action="store_true", help="Runs tests and displays useful debugging information")
		args = parser.parse_args()
		#print args
		if args.groupmembers:
			do_reportAllGroupMembers()
		elif args.group:
			do_getGroup(args.group)
		elif args.user:
			user_email = is_valid_email(args.user)
			if (user_email):
				do_user_lookup(args.user)
		elif args.input:
			input_file = os.path.join(os.getcwd(),args.input)
			do_batch_FileInfo(input_file)
		elif args.fileid:
			# do_getShareLink(args.fileid)
			do_getFileInfo(args.fileid)
		elif args.debug:
			debug = True  # Enable debugging
			bcolors.color('OKGREEN',"Debugging: On")
			do_tests()
		else:
			usage()
	except getopt.GetoptError as err:
		is_error(err)
		sys.exit(2)

if __name__ == '__main__':
	args = sys.argv[1:]
	if args:
		main(args)
	else:
		usage()
#	bcolors.color('OKGREEN',"End of Program")