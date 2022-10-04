from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from tabulate import tabulate
import pandas as pd

def main():
    fullname = input('Full Name: ')
    date = input('Date(mth dd, yyyy): ')
    guy = full(fullname)
    info = id(guy[0]['id'], date)

    print(info)

def full(f):
    people = players.find_players_by_full_name(f)
    return people

def id(x,date):
    player_info = playergamelog.PlayerGameLog(player_id=int(x), season = 2021)
    df_games = player_info.get_data_frames()[0]
    print(df_games['PlayerGameLog']['Game_ID'])
    return df_games


if __name__ == '__main__':
    main()