import requests

# Set the repository owner and name
repository_owner = "vinaynmcci"
repository_name = "newversion"

# Set the GitHub API URL
api_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/releases/latest"

# Make a GET request to the GitHub API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON response
    release_info = response.json()

    # Extract the latest version tag
    latest_version = release_info['v1.0.0']

    # Check if the latest version is different from the current version
    # You can implement a check against the current installed version here

    # Add your notification logic here (e.g., send an email, use a notification library, etc.)
    print(f"A new version ({latest_version}) is available! Visit {release_info['html_url']} for more information.")
else:
    print(f"Failed to retrieve information from GitHub. Status code: {response.status_code}")
