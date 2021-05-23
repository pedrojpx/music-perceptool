import requests
import sys
from bs4 import BeautifulSoup
from pymongo import MongoClient

def get_unique_chords(chords):
    seen = []
    unique_chords = []
    for chord in chords:
        if(chord not in seen):
            seen.append(chord)
            unique_chords.append(chord.text)
    return unique_chords

def quit_if_404(page, url):
    redirected_to_home = page.url == "https://www.cifraclub.com.br/"
    redirected_to_band = page.url.split('/')[4] == ''
    if page.status_code > 299 or redirected_to_band or redirected_to_home:
        print("Não encontrou a cifra, url usado:")
        print(url)
        quit()


artist_name = sys.argv[1].replace(" ", "-").lower()
music_name = sys.argv[2].replace(" ", "-").lower()
website_url = f'https://www.cifraclub.com.br/{artist_name}/{music_name}/'

#request page
page = requests.get(website_url)
quit_if_404(page, website_url)

#criar o objeto beautifulsoup

soup = BeautifulSoup(page.text, 'html.parser')

chords_list = []
chords = soup.find('pre')

chords = chords.find_all('b')
chords_list = get_unique_chords(chords)

# print(type(chords))
print(chords_list)
