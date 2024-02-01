import os
import requests
import zipfile
import io

def download_the_link():
    # URL of the raw GitHub file
    github_url = "https://onedrive.live.com/download?resid=9CBDB867D8AC6621%215401&authkey=!AIo_jiFU2pbcruk"
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

def download_the_assets():
    # URL of the raw GitHub file
    assets_url = "https://onedrive.live.com/download?resid=9CBDB867D8AC6621%215411&authkey=!AKE6-RC_9IeWBOQ"
    # Local path to save the downloaded file
    file_name = 'assets.zip'
    # Download the content from the GitHub link
    response = requests.get(assets_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall('.')
    os.remove(file_name)
                
def link_reader():
    link_folder = "Link"
    link_path = os.path.join(link_folder, "link.txt") 
    with open(link_path, "r") as file:
            link_content = file.read()
    return link_content

download_the_assets()
# Example usage