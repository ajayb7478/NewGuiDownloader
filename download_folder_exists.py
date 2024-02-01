import os

def folder_exists():
    return os.path.exists("Downloads") and os.path.isdir("Downloads")

