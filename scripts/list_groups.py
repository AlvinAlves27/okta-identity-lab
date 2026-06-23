"""
list_groups.py — Retrieve and display all groups from Okta Universal Directory

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

# Get all groups
response = requests.get(f"{OKTA_DOMAIN}/api/v1/groups", headers=headers)

if response.status_code == 200:
    groups = response.json()
    print(f"\nTotal Groups: {len(groups)}\n")
    print("-" * 50)

    for group in groups:
        profile = group.get('profile', {})
        print(f"Name: {profile.get('name')}")
        print(f"Description: {profile.get('description')}")
        print(f"Type: {group.get('type')}")
        print("-" * 50)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
