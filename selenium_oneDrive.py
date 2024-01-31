import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def OneDriveDownloader():
    # Get the current working directory
    current_directory = os.getcwd()
    # Define the relative path for the download folder
    download_folder = 'Downloads'
    # Combine the current directory and download folder to get the full path
    download_directory = os.path.join(current_directory, download_folder)
    # Make sure the download folder exists, create it if not
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': download_directory}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument("--start-maximized")
    # Create the Chrome WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://onedrive.live.com/?authkey=%21AE1AEEgJY3nICos&id=9CBDB867D8AC6621%215400&cid=9CBDB867D8AC6621&parId=root&parQt=sharedby&o=OneUp")       
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".od-Button-label.od-ButtonBarCommand-label")))
        element.click()        
        time.sleep(3)
    except Exception as e:
        print(f"Error: {e}")  
        input("")       
    driver.get("chrome://downloads/")  
    input("")  
           
OneDriveDownloader()
    