#!/usr/bin/env python3

"""
EXPORT THE BLOCK-ASSIGNMENT FILE FOR A DRA MAP BY ID

For example:

$ scripts-1time/export_map.py TODO

For documentation, type:

$ scripts-1time/export_map.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
import os, time

from typing import Any, Dict

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from rdabase import require_args

from constants import OFFICIAL_MAP_PROXIES


def submit_url_to_headless_browser(url: str, sleep: int = 10) -> None:
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
        time.sleep(sleep)  # Wait for 10 seconds
    finally:
        # Close the browser
        driver.quit()


def main() -> None:
    """Export the block-assignment file for a DRA map by ID."""

    # Parse the command-line arguments
    args: argparse.Namespace = parse_args()

    guid: str = OFFICIAL_MAP_PROXIES[args.state][args.plantype.lower()]

    export_url: str = f"https://davesredistricting.org/export/{guid}.csv"
    # Submit the URL to the headless browser
    # submit_url_to_headless_browser(args.url)
    submit_url_to_headless_browser(export_url, args.sleep)

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a ratings table (CSV) for the notable maps for a state & type of plan."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--plantype",
        help="The type of plan (congress, upper, lower)",
        type=str,
    )
    parser.add_argument(
        "--name",
        type=str,
        help="The name for the block-assignment file",
    )
    parser.add_argument(
        "--sleep",
        type=int,
        default=10,
        help="How many seconds to sleep while waiting for the download.",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "state": "NC",
        "plantype": "Congress",
        "name": "NC_2022_Congress_Official_Proxy.csv",
        "output": "temp",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
