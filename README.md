# 🌍 Ubuntu-Inspired Image Fetcher

**Wisdom of Ubuntu**: *"I am because we are."*

This Python program is inspired by the Ubuntu philosophy. It connects to the global web community, respectfully fetches shared images, and organizes them for later use.  

---

## ✨ Features
- Prompts the user for one or more image URLs.  
- Creates a directory called **Fetched_Images** (if it doesn’t already exist).  
- Downloads and saves the images with safe filenames.  
- Prevents duplicates to avoid overwriting.  
- Validates that the file is an image and checks its size.  
- Handles errors (timeouts, invalid URLs, non-images) gracefully.  

---

## 🛠️ Requirements
- Python 3.x  
- Libraries:  
  - `requests`  
  - `os`  
  - `urllib.parse`  

Install requests if not available:  
```bash
pip install requests
