#!/usr/bin/env python3

"""
EXPORT THE BLOCK-ASSIGNMENT FILE FOR A DRA MAP BY ID

For example:

$ scripts-1time/export_map.py TODO

For documentation, type:

$ scripts-1time/export_map.py -h

"""

import argparse, os, time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def submit_url_to_headless_browser(url):
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensures GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set download directory to user's Downloads folder
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)
        print(f"Executed URL: {url}")
        print(f"Downloads will be saved to: {download_dir}")

        # Wait for a bit to allow any downloads to complete
        # Adjust the sleep time based on expected download size and internet speed
        time.sleep(10)  # Wait for 10 seconds
    finally:
        # Close the browser
        driver.quit()


def main() -> None:
    """Export the block-assignment file for a DRA map by ID."""

    # Parse the command-line arguments
    # args: argparse.Namespace = parse_args()

    # Submit the URL to the headless browser
    # submit_url_to_headless_browser(args.url)
    submit_url_to_headless_browser(
        "https://davesredistricting.org/export/a457887e-f932-4186-a14c-0d94f781e575.csv"
    )

    pass


if __name__ == "__main__":
    main()

### END ###
