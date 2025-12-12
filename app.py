import pandas as pd
import requests

# Define the API endpoint and headers
url = "https://active-jobs-db.p.rapidapi.com/active-ats-7d"

headers = {
    "X-RapidAPI-Key": "Your_RapidAPI_Key_Here",
    "X-RapidAPI-Host": "active-jobs-db.p.rapidapi.com"
}


params = params = {
    "offset": "0",
    "limit": "10",
    "title_filter": "Data Engineer",
    "location_filter": "United States",
    "description_type": "text"
}


# Function to fetch data from API and save to CSV
def json_to_csv():
    df = pd.DataFrame()
    for i in range(1, 11):
        url = "https://active-jobs-db.p.rapidapi.com/active-ats-7d"
        headers = {
    "X-RapidAPI-Key": "Your_RapidAPI_Key_Here",
    "X-RapidAPI-Host": "active-jobs-db.p.rapidapi.com"
        }
        params = params = {
    "offset": "0",
    "limit": "30",
    "title_filter": "Data Engineer",
    "location_filter": "United States",
    "description_type": "text"
    }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                temp_df = pd.DataFrame(data)
                usecols = ["date_posted","title","organization","description_text"]
                temp_df = temp_df[usecols]
                df = pd.concat([df, temp_df], ignore_index=True)
            else:
                print("Unexpected response format:", data)
        else:
            print(f"API request failed with status code {response.status_code}: {response.text}")

# Save the DataFrame to a CSV file
    df.to_csv('UpworkJobs.csv', index=False)
    return df


# Reading from the CSV file
file_path = 'UpworkJobs.csv'
df = pd.read_csv(file_path)
print(df)



