import os
import requests

def download_the_link():
    # URL of the raw GitHub file
    #github_url = "https://github.com/ajayb7478/ajayb7478.github.io/raw/main/link.txt"
    github_url = "https://drive.usercontent.google.com/uc?id=16Prcr-h-o3yVuQK2yJnobvZ0_Tto4A82&export=download"
    #https://drive.usercontent.google.com/uc?id=16Prcr-h-o3yVuQK2yJnobvZ0_Tto4A82&export=download  = link downloader
    #https://drive.usercontent.google.com/download?id=10eHbV3t3lxGAQkpILwrMbAcwj7xMuL5A&export=download&authuser=0 actual file
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
    else:
        # If the download was unsuccessful, print an error message
        print(f"Failed to download link.txt. Status code: {response.status_code}")

def link_reader():
    link_folder = "Link"
    link_path = os.path.join(link_folder, "link.txt") 
    with open(link_path, "r") as file:
            link_content = file.read()
    return link_content

# Example usage