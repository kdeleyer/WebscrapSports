from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def home(request):
    return HttpResponse("Welcome to the home page!")


def get_live_sports():
    url = 'https://www.espn.com/'  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    games = []

    # Adjust selectors based on the actual HTML structure of the website
    for game in soup.find_all('div', class_='live-game'):
        title = game.find('div', class_='game-title').text if game.find('div', class_='game-title') else 'N/A'
        time = game.find('span', class_='game-time').text if game.find('span', class_='game-time') else 'N/A'
        teams = game.find_all('span', class_='team-name')

        if teams and len(teams) == 2:
            team1 = teams[0].text.strip()
            team2 = teams[1].text.strip()
        else:
            team1 = 'N/A'
            team2 = 'N/A'

        games.append({
            'title': title,
            'time': time,
            'team1': team1,
            'team2': team2
        })

    return games



def sports_view(request):
    games = get_live_sports()
    today = datetime.today().strftime('%Y-%m-%d')
    context = {
        'today': today,
        'games': games
    }
    return render(request, 'sports.html', context)

