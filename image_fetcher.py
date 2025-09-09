"""
Ubuntu-Inspired Image Fetcher

This script downloads one or more images from user-provided URLs,
stores them in a Fetched_Images directory, and ensures safe filenames,
size checks, and error handling in line with Ubuntu principles.
"""

import os
import requests
from urllib.parse import urlparse


# Constants
SAVE_DIR = "Fetched_Images"
CHUNK_SIZE = 8192
TIMEOUT = 8  # seconds
MAX_SIZE_MB = 8  # maximum allowed file size in megabytes


def safe_filename(url, fallback="ubuntu_image.jpg"):
    """
    Generate a safe filename from a URL or use a fallback.
    Only allows alphanumeric characters, dots, dashes, and underscores.
    """
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    if not name:
        name = fallback
    safe = "".join(c for c in name if c.isalnum() or c in "._-")
    return safe if safe else fallback


def fetch_and_store(url, save_dir=SAVE_DIR, max_size=MAX_SIZE_MB):
    """
    Download a single image from the web and store it safely.

    Args:
        url (str): The URL of the image to download.
        save_dir (str): The directory where images are stored.
        max_size (int): Maximum allowed file size in MB.
    """
    try:
        response = requests.get(url, stream=True, timeout=TIMEOUT)
        response.raise_for_status()

        # Verify content type
        ctype = response.headers.get("Content-Type", "")
        if not ctype.startswith("image/"):
            print(f"⚠️  Skipped: {url} is not an image ({ctype})")
            return

        # Check file size if available
        length = response.headers.get("Content-Length")
        if length and int(length) > max_size * 1024 * 1024:
            print(f"⚠️  Skipped: {url} is too large (> {max_size}MB)")
            return

        # Prepare file path
        filename = safe_filename(url)
        filepath = os.path.join(save_dir, filename)

        if os.path.exists(filepath):
            print(f"ℹ️  Already exists: {filename}")
            return

        # Save in chunks
        with open(filepath, "wb") as file:
            for block in response.iter_content(CHUNK_SIZE):
                file.write(block)

        print(f"✅ Saved: {filename}")

    except requests.exceptions.Timeout:
        print(f"⏳ Timeout while fetching {url}")
    except requests.exceptions.RequestException as err:
        print(f"❌ Could not fetch {url}: {err}")


def main():
    """Main entry point of the program."""
    print("🌍 Ubuntu Image Collector")
    print("Collecting and organizing shared images with respect.\n")

    urls = input("Enter one or more image URLs (separated by spaces): ").split()

    os.makedirs(SAVE_DIR, exist_ok=True)

    for link in urls:
        if link.strip():
            fetch_and_store(link.strip())


if __name__ == "__main__":
    main()