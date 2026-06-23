"""
list_users.py — Retrieve and display all users from Okta Universal Directory

Part of the Okta Identity Lab — Part 6: API & Code Automation
https://github.com/AlvinAlves27/okta-identity-lab
"""

import requests
import json

# Configuration
OKTA_DOMAIN = "https://integrator-9692338.okta.com"
API_TOKEN = "YOUR_API_TOKEN"  # Replace with your actual token

headers = {
    "Authorization": f"SSWS {API_TOKEN}",
    "Content-Type": "application/json"
}

# Get all users
response = requests.get(f"{OKTA_DOMAIN}/api/v1/users", headers=headers)

if response.status_code == 200:
    users = response.json()
    print(f"\nTotal Users: {len(users)}\n")
    print("-" * 80)

    for user in users:
        profile = user.get('profile', {})
        print(f"Name: {profile.get('firstName')} {profile.get('lastName')}")
        print(f"Email: {profile.get('email')}")
        print(f"Status: {user.get('status')}")
        print(f"Department: {profile.get('department', 'N/A')}")
        print(f"User Type: {profile.get('userType', 'N/A')}")
        print("-" * 80)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
