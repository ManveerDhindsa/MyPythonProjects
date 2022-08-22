#this program returns the players average stats for the latest season

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from tabulate import tabulate


def main():
    fullname = input('Full Name: ')
    guy = full(fullname)
    info = id(guy[0]['id'])
    infodazz = stat(info)
    dazz = [infodazz['headers'], infodazz['data'][0]]
    print(tabulate(dazz, tablefmt="grid"))

def full(f):
    people = players.find_players_by_full_name(f)
    return people

def id(x):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=int(x))
    return player_info

def stat(y):
    test = y.player_headline_stats.get_dict()
    return test


if __name__ == '__main__':
    main()