"""
For scraping the website of the files i needed. Did not want to have to download
100+ files manually.
This only needs to be run once!!!. 
"""
import requests
from bs4 import BeautifulSoup
import os


def fetch_files():
    """
    Downloads all the hourly files from the website, 
    and creates a directory called 'hourly_data_files'
    that will contain all hourly files. 
    """
    url = 'https://bri3.fvh.io/opendata/ulkokuntosali/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')

        os.makedirs('hourly_data_files', exist_ok=True)

        for link in links:
            file_url = link.get('href')

            if file_url and "hourly" in file_url and file_url.endswith('.csv.gz'):  #  hourly CSV files

                if not file_url.startswith('http'):
                    file_url = url + file_url

                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    file_name = os.path.join('hourly_data_files', file_url.split('/')[-1])
                    with open(file_name, 'wb') as file:
                        file.write(file_response.content)
                else:
                    print(f'Failed to download: {file_url} (Status code: {file_response.status_code})')
    else:
        print(f'Failed to retrieve webpage. Status code: {response.status_code}')
