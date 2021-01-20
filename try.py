import requests
import base64
import pandas as pd

client_id = '86ceb770de7b43f9b75d341b77367da0'
client_secret = '59914a1a8c7c469fb1bf18a3e42b2b5c'

client_creds = f'{client_id}:{client_secret}'
client_creds_b64 = base64.b64encode(client_creds.encode())

#I need to send the ENCODED base64 body params with the POST method
# Ex:  a = mystring.encode('utf-8')
# base64.b64encode(a)

#Body params required for POST

token_data = {
'grant_type' : 'client_credentials'
}

header_data = { 
'Authorization': f'Basic {client_creds_b64.decode()}' 
}

#What is the URL i need to POST to?

post_url = 'https://accounts.spotify.com/api/token'
get_url = 'https://api.spotify.com/v1/artists/25mFVpuABa9GkGcj9eOPce/top-tracks?country=RO'

#Try to Authorize

r = requests.post(post_url, data=token_data, headers=header_data)
print(r.json())

#Sort authorization token

auth_data = r.json()
auth_token = auth_data['access_token']
auth_token_type = auth_data['token_type']

look_up_headers = {
'Authorization': f'Bearer {auth_token}'
}

look_up_artist = requests.get(get_url, headers=look_up_headers)
print(look_up_artist.json())


#Sort the JSON data in Pandas and print the track names
raw_data = pd.DataFrame(look_up_artist.json())
track_list = []
for i in raw_data['tracks']:
	track_list.append(i['name'])
	
for i in track_list:
	print(i)


