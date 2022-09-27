# this program will make decisions based on the year and season of anime you want to get a recommendation from
# Also will be getting the users perferred genre
# We will use Jikan API and display the options in a table using Pandas and tabulate
# Random will make a choice for the user based upon the score/rating of the show and recommend an anime with a score above 7.00
# if no choice is high quality enough for the year, season, genre entered then the program will let you know that there is no recommendation high quality enough and will end the code
# below shows a dictionary of one of the animes that shows up in the dataset
"""{'mal_id': 52551, 'url': 'https://myanimelist.net/anime/52551/Futsal_Boys_Short_Anime', 'title': 'Futsal Boys!!!!! Short Anime', 'image_url': 'https://cdn.myanimelist.net/images/anime/1999/126129.jpg', 
'synopsis': 'New short anime focusing on all the different members of futsal teams. Included in the 6th Blu-ray/DVD volume.', 'type': None, 'airing_start': '2022-09-27T15:00:00+00:00', 'episodes': 5, 'members': 353, 'genres': [{'mal_id': 4, 'type': 'anime', 'name': 'Comedy', 'url': 'https://myanimelist.net/anime/genre/4/Comedy'}, {'mal_id': 30, 'type': 'anime', 'name': 'Sports', 'url': 'https://myanimelist.net/anime/genre/30/Sports'}], 'explicit_genres': [], 'themes': [{'mal_id': 77, 'type': 'anime', 'name': 'Team Sports', 'url': 'https://myanimelist.net/anime/genre/77/Team_Sports'}], 'demographics': [], 'source': 'Mixed media', 'producers': [{'mal_id': 51, 'type': 'anime', 'name': 'Diomedéa', 'url': 'https://myanimelist.net/anime/producer/51/Diomed%C3%A9a'}], 'score': None, 'licensors': [], 'r18': False, 'kids': False, 'continuing': False}
 """
import random
from jikanpy import Jikan
import pandas as pd
from tabulate import tabulate
jikan = Jikan()

choices = []

year_ = input('Enter the year you want to get an anime recommendation from (2020, 2019, ...): ')
season_ = input('Enter the season you want to get an anime recommendation from (summer, winter, fall, spring): ').lower()
genre = input('Enter the your preferred genre: ').title()

anime_options = jikan.season(year = year_, season = season_)

a = anime_options['anime']
anime_folder = []
id_folder = []
genre_folder = []

for i in range(len(a)):
    hold = []
    for j in range(len(a[i]['genres'])):
        hold.append(a[i]['genres'][j]['name'])
    total = ' '.join(hold)
    if genre in total:
        genre_folder.append(total)
        anime_folder.append(a[i]['title'])
        id_folder.append(a[i]['mal_id'])
    
    
data = {'Anime Name': anime_folder, 'ID': id_folder, 'Genre': genre_folder}
df = pd.DataFrame(data)
print(tabulate(df, headers='keys', tablefmt='psql'))

# making a random choice and checking if it is above a 7.00 score and continuing until it is and giving the recommendation

stat = 0.00
iter = -2
while True:
    option = random.choice(id_folder)
    iter += 1
    if iter > len(id_folder):
         raise ValueError('Either no ratings exist for this season yet or no choice is high quality enough to recommend in this section of anime and genre')
    stats = jikan.anime(option, extension='')
    stat = stats['score']
    if stat == None:
        continue
    if float(stat) < 7.00:
        continue
    else:
        titles = jikan.anime(option, extension='')
        title = titles['title_english']
        print('We recommend: ', title)
        break