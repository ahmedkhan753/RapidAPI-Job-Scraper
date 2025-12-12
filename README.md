# RapidAPI-Job-Scraper
# Data-Extraction-Pipeline

## 📄 Overview
This project is a Python data pipeline designed for programmatic job data acquisition. It uses the **requests** library to efficiently interface with the **Active Jobs DB API** on RapidAPI and **pandas** for structuring and cleaning the output. The pipeline demonstrates automated handling of API authentication, parameterization, and pagination to extract large datasets.

## ⚙️ Setup and Configuration

### Prerequisites
* Python 3.x
* The `requests` and `pandas` libraries (`pip install requests pandas`).
* A valid **RapidAPI Key** with an active subscription to the target API (`active-jobs-db.p.rapidapi.com`).

### Configuration
Update the `HEADERS` dictionary in your main script with your unique credentials:

```python
HEADERS = {
    "X-RapidAPI-Key": "YOUR_UNIQUE_RAPIDAPI_KEY", 
    "X-RapidAPI-Host": "active-jobs-db.p.rapidapi.com"
}
