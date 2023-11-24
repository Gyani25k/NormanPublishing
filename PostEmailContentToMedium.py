import requests
import nbformat

# Your Medium Integration Token
token = '266b17e32109182687f6ce98bcbb39922156fb546c6ae876294422a3e07bd13ae'

user_info = requests.get(f"https://api.medium.com/v1/me?accessToken={token}")
user_json_info = user_info.json()
print(user_json_info)

# Your Medium user ID (you can find it in the URL when logged into Medium)
user_id = '181d511e5cee47a7c1e757d4c4e91a9285fd12423d9a0e843e251846cbdbf47ab'

# URL for creating a post on Medium
medium_api_url = f'https://api.medium.com/v1/users/{user_id}/posts'

# Headers with the necessary authorization information
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}

# Content of your email.html
with open('email.html', 'r', encoding='utf-8') as file:
    email_content = file.read()


# Data to be posted
post_data = {
    'title': "Notebook to Email to Medium",
    'contentFormat': 'html',
    'content': email_content,
    'publishStatus': 'public',  # Adjust as needed (e.g., 'draft' for a draft)
}

# Make the API request
response = requests.post(medium_api_url, json=post_data, headers=headers)

# Check the response
if response.status_code == 201:
    print('Post published successfully!')
else:
    print(f'Error: {response.status_code} - {response.text}')
