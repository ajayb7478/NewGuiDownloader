import requests
from tqdm import tqdm

def download_file_with_progress(url, destination):
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('content-length', 0))
    
    # Define the chunk size for downloading
    chunk_size = 1024  # 1 KB

    # Create a progress bar using tqdm
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

    with open(destination, 'wb') as file:
        for data in response.iter_content(chunk_size=chunk_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

# Replace 'your_link_here' with the actual link you have
file_url = 'https://drive.usercontent.google.com/download?id=10eHbV3t3lxGAQkpILwrMbAcwj7xMuL5A&export=download&authuser=0&confirm=t&uuid=1f8d824f-00b4-4c68-8ae9-22e65d5c0523&at=APZUnTW9P0X3SOGi7Q40nG1wgxHG%3A1706442013448'

# Replace 'destination_file_name' with the desired name for the downloaded file
destination_file_name = 'downloads/Rocket Flyer.zip'

download_file_with_progress(file_url, destination_file_name)
