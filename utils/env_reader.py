import os
from dotenv import load_dotenv


load_dotenv()

def get_url():
    url = os.getenv("URL")
    return url

def get_browser():
    browser = os.getenv("BROWSER")  # chromium/firefox/webkit
    return browser
