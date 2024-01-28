import os
import requests

def download_and_read_link():
    # URL of the raw GitHub file
    github_url = "https://github.com/ajayb7478/ajayb7478.github.io/raw/main/link.txt"

    # Local path to save the downloaded file
    local_folder = "Link"
    local_path = os.path.join(local_folder, "link.txt")

    # Create the "Link" folder if it doesn't exist
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
        
    # Download the content from the GitHub link
    response = requests.get(github_url)

    # Check if the download was successful (status code 200)
    if response.status_code == 200:
        # Write the content to the local file
        with open(local_path, "wb") as file:
            file.write(response.content)

        # Read the content from the local file
        with open(local_path, "r") as file:
            link_content = file.read()

        # Return the content
        return link_content
    else:
        # If the download was unsuccessful, print an error message
        print(f"Failed to download link.txt. Status code: {response.status_code}")
        return None

# Example usage