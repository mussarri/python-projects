from bs4 import BeautifulSoup
import requests 
import pandas as pd


job_titles = []
companies = []
locations = []
dates = []

def get_data():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        job_cards = soup.find_all('div', class_='card-content')
        for card in job_cards:
            job_titles.append(card.find('h2', class_='title').text.strip() or '-')
            companies.append(card.find('h3', class_='company').text.strip() or '-')
            locations.append(card.find('p', class_='location').text.strip() or '-')
            dates.append(card.find('time').text.strip() or '-')
    
try:   
    get_data()
    df = pd.DataFrame(data = {
        'Titles':job_titles[0:4],
        'Companies':companies[0:4],
        'Locations':locations[0:4],
        'Dates':dates[0:4]
    })

    print(df)  
except Exception as e:
    print(e)
