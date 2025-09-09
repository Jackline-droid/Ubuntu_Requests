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

🚀 How to Run
python ubuntu_fetcher.py

🖥️ Sample Run
$ python ubuntu_fetcher.py
🌍 Ubuntu Image Collector
Collecting and organizing shared images with respect.

Enter one or more image URLs (separated by spaces): 
https://www.example.com/sample1.jpg https://www.example.com/sample2.png

✅ Saved: sample1.jpg
✅ Saved: sample2.png


If you run the program again with the same URLs:

ℹ️  Already exists: sample1.jpg
ℹ️  Already exists: sample2.png


If you provide a non-image URL:

⚠️  Skipped: https://www.example.com/index.html is not an image (text/html)


If the file is too large:

⚠️  Skipped: https://www.example.com/huge.jpg is too large (> 8MB)
