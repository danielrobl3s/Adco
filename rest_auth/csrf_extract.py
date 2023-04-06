import requests
import json
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Set the URL for the clients endpoint
url = "http://127.0.0.1:8000/module/clients/"

# Get the currently logged-in user's username
username = get_user_model().objects.get(username='your_username')

# Get the user's token from the database
token = Token.objects.get(user__username=username).key

# Set headers with the user's token
headers = {'Authorization': 'Token {}'.format(token)}

# Send a GET request to the clients endpoint with headers
response = requests.get(url, headers=headers)

# Extract the CSRF token from the response cookies
csrftoken = response.cookies.get('csrftoken')

# Extract the clients data from the response JSON
clients = json.loads(response.text)

# Print the CSRF token and clients data
print("CSRF Token: ", csrftoken)
print("Clients: ", clients)
