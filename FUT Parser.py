import requests
import csv
from bs4 import BeautifulSoup as bs
import time
import socks
import socket
from TorCrawler import TorCrawler


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}

base_url = 'https://www.futbin.com/20/player/1'


def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = bs(ip, 'html.parser')
    print(soup.find('body').text)


#socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
#socket.socket = socks.socksocket
# Создаём свой краулер, в опциях вводим пароль
crawler = TorCrawler(ctrl_pass='formula1')
checkIP()


def fb_parse(base_url, headers):
    x = 0
    z1 = 1
    z2 = 6
    start = time.time()
    players = []
    urls = []
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        request = session.get('https://www.futbin.com/players?page=1&version=gold', headers=headers)
        soup = bs(request.content, 'lxml')
        try:
            ulr = soup.find_all('a', attrs={'class': 'player_name_players_table'})
            print(ulr)
        except:
            pass
        for i in range(z1, z2):
            url = f'https://www.futbin.com/20/player/{i}'
            if url not in urls:
                urls.append(url)
    for url in urls:
        x += 1
        y = round(((x / (z2 - z1 + 1)) * 100), 2)
        print(y, '%')
        try:
            #checkIP()
            time.sleep(5)
            request = session.get(url, headers=headers)
            soup = bs(request.content, 'lxml')
            rating = soup.find('h1', attrs={'class': 'player_header header_top pb-0'}).text.split()
            name = soup.find('span', attrs={'class': 'header_name'}).text
            position = soup.find('div', attrs={'class': 'pcdisplay-pos'}).text
            club = soup.find_all('td', attrs={'class': 'table-row-text'})[1].text.split()
            nation = soup.find_all('td', attrs={'class': 'table-row-text'})[2].text.split()
            league = soup.find_all('td', attrs={'class': 'table-row-text'})[3].text.split()
            skills = soup.find_all('td', attrs={'class': 'table-row-text'})[4].text.split()
            weak_foot = soup.find_all('td', attrs={'class': 'table-row-text'})[5].text.split()
            a = len(soup.find_all('td', attrs={'class': 'table-row-text'}))
            foot = soup.find_all('td', attrs={'class': 'table-row-text'})[7].text.split()
            height = soup.find_all('td', attrs={'class': 'table-row-text'})[8].text.split('c')
            weight = soup.find_all('td', attrs={'class': 'table-row-text'})[9].text.split()
            revision = soup.find_all('td', attrs={'class': 'table-row-text'})[10].text
            def_wr = soup.find_all('td', attrs={'class': 'table-row-text'})[11].text
            att_wr = soup.find_all('td', attrs={'class': 'table-row-text'})[12].text
            traits = soup.find('div', attrs={'id': 'traits_content'}).text.split()
            pace = soup.find('div', attrs={'id': 'main-pace-val-0'}).text.split()
            acceleration = soup.find('div', attrs={'id': 'sub-acceleration-val-0'}).text.split()
            sprint_speed = soup.find('div', attrs={'id': 'sub-sprintspeed-val-0'}).text.split()
            shooting = soup.find('div', attrs={'id': 'main-shooting-val-0'}).text.split()
            positioning = soup.find('div', attrs={'id': 'sub-positioning-val-0'}).text.split()
            finishing = soup.find('div', attrs={'id': 'sub-finishing-val-0'}).text.split()
            shot_power = soup.find('div', attrs={'id': 'sub-shotpower-val-0'}).text.split()
            long_shots = soup.find('div', attrs={'id': 'sub-longshotsaccuracy-val-0'}).text.split()
            volleys = soup.find('div', attrs={'id': 'sub-volleys-val-0'}).text.split()
            penalties = soup.find('div', attrs={'id': 'sub-penalties-val-0'}).text.split()
            passing = soup.find('div', attrs={'id': 'main-passing-val-0'}).text.split()
            vision = soup.find('div', attrs={'id': 'sub-vision-val-0'}).text.split()
            crossing = soup.find('div', attrs={'id': 'sub-crossing-val-0'}).text.split()
            fk_acc = soup.find('div', attrs={'id': 'sub-freekickaccuracy-val-0'}).text.split()
            short_passing = soup.find('div', attrs={'id': 'sub-shortpassing-val-0'}).text.split()
            long_passing = soup.find('div', attrs={'id': 'sub-longpassing-val-0'}).text.split()
            curve = soup.find('div', attrs={'id': 'sub-curve-val-0'}).text.split()
            dribbling_m = soup.find('div', attrs={'id': 'main-dribblingp-val-0'}).text.split()
            agility = soup.find('div', attrs={'id': 'sub-agility-val-0'}).text.split()
            balance = soup.find('div', attrs={'id': 'sub-balance-val-0'}).text.split()
            reactions = soup.find('div', attrs={'id': 'sub-reactions-val-0'}).text.split()
            ball_control = soup.find('div', attrs={'id': 'sub-ballcontrol-val-0'}).text.split()
            dribbling = soup.find('div', attrs={'id': 'sub-dribbling-val-0'}).text.split()
            composure = soup.find('div', attrs={'id': 'sub-composure-val-0'}).text.split()
            defending = soup.find('div', attrs={'id': 'main-defending-val-0'}).text.split()
            interceptions = soup.find('div', attrs={'id': 'sub-interceptions-val-0'}).text.split()
            heading_accuracy = soup.find('div', attrs={'id': 'sub-headingaccuracy-val-0'}).text.split()
            marking = soup.find('div', attrs={'id': 'sub-marking-val-0'}).text.split()
            standing_tackle = soup.find('div', attrs={'id': 'sub-standingtackle-val-0'}).text.split()
            sliding_tackle = soup.find('div', attrs={'id': 'sub-slidingtackle-val-0'}).text.split()
            physicality = soup.find('div', attrs={'id': 'main-heading-val-0'}).text.split()
            jumping = soup.find('div', attrs={'id': 'sub-jumping-val-0'}).text.split()
            stamina = soup.find('div', attrs={'id': 'sub-stamina-val-0'}).text.split()
            strength = soup.find('div', attrs={'id': 'sub-strength-val-0'}).text.split()
            aggression = soup.find('div', attrs={'id': 'sub-aggression-val-0'}).text.split()
            att_wr_rate = 0
            def_wr_rate = 0
            if att_wr == 'High':
                att_wr_rate = 1
            elif att_wr == 'Med':
                att_wr_rate = 0.66
            elif att_wr == 'Low':
                att_wr_rate = 0.33
            if def_wr == 'High':
                def_wr_rate = 1
            elif def_wr == 'Med':
                def_wr_rate = 0.66
            elif def_wr == 'Low':
                def_wr_rate = 0.33
            skill_rate = int(skills[0]) * 0.2
            weak_foot_rate = int(weak_foot[0]) * 0.2
            best_cb = round(
                ((int(acceleration[0]) * 0.1 + int(sprint_speed[0]) * 0.1 + int(agility[0]) * 0.07 +
                  int(balance[0]) * 0.07 + int(interceptions[0]) * 0.07 + int(heading_accuracy[0]) * 0.07 +
                  int(marking[0]) * 0.07 + int(standing_tackle[0]) * 0.07 + int(sliding_tackle[0]) * 0.07 +
                  int(jumping[0]) * 0.07 + int(strength[0]) * 0.07 +
                  int(aggression[0]) * 0.07) / 12) + (int(height[0])) / 100, 5)
            best_fb = round(
                ((int(acceleration[0]) * 0.08 + int(sprint_speed[0]) * 0.08 + int(crossing[0]) * 0.07 +
                  int(long_passing[0]) * 0.07 + int(curve[0]) * 0.07 + int(agility[0]) * 0.07 +
                  int(balance[0]) * 0.07 + int(interceptions[0]) * 0.07 + int(marking[0]) * 0.07 +
                  int(standing_tackle[0]) * 0.07 + int(jumping[0]) * 0.07 +
                  int(stamina[0]) * 0.07 + int(strength[0]) * 0.07) / 13) + (int(height[0])) / 100, 5)
            best_cdm = round(
                ((int(acceleration[0]) * 0.1 + int(sprint_speed[0]) * 0.1 + int(shot_power[0]) * 0.1 +
                  int(long_shots[0]) * 0.1 + int(short_passing[0]) * 0.1 + int(interceptions[0]) * 0.1 +
                  int(marking[0]) * 0.1 + int(stamina[0]) * 0.1 + int(strength[0]) * 0.1 +
                  int(aggression[0]) * 0.1) / 10 + att_wr_rate + def_wr_rate + (int(height[0])) / 100), 5)
            best_cm = round(
                ((int(acceleration[0]) * 0.08 + int(sprint_speed[0]) * 0.08 + int(shot_power[0]) * 0.07 +
                  int(long_shots[0]) * 0.07 + int(vision[0]) * 0.07 + int(short_passing[0]) * 0.07 +
                  int(long_passing[0]) * 0.07 + int(curve[0]) * 0.07 + int(agility[0]) * 0.07 +
                  int(ball_control[0]) * 0.07 + int(dribbling[0]) * 0.07 + int(interceptions[0]) * 0.07 +
                  int(stamina[0]) * 0.07 + int(strength[0]) * 0.07) / 14 + att_wr_rate +
                 def_wr_rate + weak_foot_rate), 5)
            best_cam = round(
                ((int(acceleration[0]) * 0.08 + int(sprint_speed[0]) * 0.08 + int(finishing[0]) * 0.06 +
                  int(long_shots[0]) * 0.06 + int(vision[0]) * 0.06 + int(crossing[0]) * 0.06 +
                  int(short_passing[0]) * 0.06 + int(long_passing[0]) * 0.06 + int(curve[0]) * 0.06 +
                  int(agility[0]) * 0.06 + int(balance[0]) * 0.06 + int(reactions[0]) * 0.06 +
                  int(ball_control[0]) * 0.06 + int(dribbling[0]) * 0.06 + int(composure[0]) * 0.06 +
                  int(stamina[0]) * 0.06) / 16 + skill_rate + weak_foot_rate), 5)
            best_w = round(
                ((int(acceleration[0]) * 0.1 + int(sprint_speed[0]) * 0.1 + int(positioning[0]) * 0.08 +
                  int(finishing[0]) * 0.08 + int(crossing[0]) * 0.08 + int(long_passing[0]) * 0.08 +
                  int(curve[0]) * 0.08 + int(agility[0]) * 0.08 + int(ball_control[0]) * 0.08 +
                  int(dribbling[0]) * 0.08 + int(stamina[0]) * 0.08 + int(strength[0]) * 0.08)
                 / 12 + skill_rate + weak_foot_rate + att_wr_rate + (int(height[0])) / 100), 5)
            best_st = round(
                ((int(acceleration[0]) * 0.1 + int(sprint_speed[0]) * 0.1 + int(positioning[0]) * 0.06 +
                  int(finishing[0]) * 0.06 + int(vision[0]) * 0.06 + int(short_passing[0]) * 0.06 +
                  int(agility[0]) * 0.06 + int(reactions[0]) * 0.06 + int(ball_control[0]) * 0.06 +
                  int(dribbling[0]) * 0.06 + int(composure[0]) * 0.06 + int(heading_accuracy[0]) * 0.06 +
                  int(jumping[0]) * 0.06 + int(stamina[0]) * 0.06 + int(strength[0]) * 0.06) / 15 +
                 skill_rate + weak_foot_rate + att_wr_rate), 5)
            players.append({
                'rating': rating[0],
                'player_name': name,
                'position': position,
                'club': ' '.join(club),
                'nation': ' '.join(nation),
                'league': ' '.join(league),
                'skills': round(skill_rate, 1),
                'weak_foot': round(weak_foot_rate, 1),
                'foot': foot[0],
                'height': int(height[0]) / 100,
                'weight': weight[0],
                'revision': revision,
                'def_wr': def_wr_rate,
                'att_wr': att_wr_rate,
                'traits': ' '.join(traits),
                'pace': pace[0],
                'acceleration': acceleration[0],
                'sprint_speed': sprint_speed[0],
                'shooting': shooting[0],
                'positioning': positioning[0],
                'finishing': finishing[0],
                'shot_power': shot_power[0],
                'long_shots': long_shots[0],
                'volleys': volleys[0],
                'penalties': penalties[0],
                'passing': passing[0],
                'vision': vision[0],
                'crossing': crossing[0],
                'fk_acc': fk_acc[0],
                'short_passing': short_passing[0],
                'long_passing': long_passing[0],
                'curve': curve[0],
                'dribbling_m': dribbling_m[0],
                'agility': agility[0],
                'balance': balance[0],
                'reactions': reactions[0],
                'ball_control': ball_control[0],
                'dribbling': dribbling[0],
                'composure': composure[0],
                'defending': defending[0],
                'interceptions': interceptions[0],
                'heading_accuracy': heading_accuracy[0],
                'marking': marking[0],
                'standing_tackle': standing_tackle[0],
                'sliding_tackle': sliding_tackle[0],
                'physicality': physicality[0],
                'jumping': jumping[0],
                'stamina': stamina[0],
                'strength': strength[0],
                'aggression': aggression[0],
                'best_cb': best_cb,
                'best_fb': best_fb,
                'best_cdm': best_cdm,
                'best_cm': best_cm,
                'best_cam': best_cam,
                'best_w': best_w,
                'best_st': best_st,
                'url': url
            })
        except:
            pass
    else:
        print('ERROR or Done. Status code = ' + str(request.status_code))
    end = time.time()
    result = round(((end - start) / 60), 2)
    print(result)
    return players


def files_writer(players):
    with open('parsed_player_database.csv', 'a', encoding='utf-8', newline='') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Rating',
                        'Name',
                        'Position',
                        'Club',
                        'Nation',
                        'League',
                        'Skill Moves',
                        'Weak Foot',
                        'Foot',
                        'Height',
                        'Weight',
                        'Revision',
                        'Def WR',
                        'Att WR',
                        'Traits',
                        'PACE',
                        'Acceleration',
                        'Sprint Speed',
                        'SHOOTING',
                        'Positioning',
                        'Finishing',
                        'Shot Power',
                        'Long Shots',
                        'Volleys',
                        'Penalties',
                        'PASSING',
                        'Vision',
                        'Crossing',
                        'FK.Accuracy',
                        'Short Passing',
                        'Long Passing',
                        'Curve',
                        'DRIBBLING',
                        'Agility',
                        'Balance',
                        'Reactions',
                        'Ball Control',
                        'Dribbling',
                        'Composure',
                        'DEFENDING',
                        'Interceptions',
                        'Heading Accuracy',
                        'Marking',
                        'Standing Tackle',
                        'Sliding Tackle',
                        'PHYSICALITY',
                        'Jumping',
                        'Stamina',
                        'Strength',
                        'Aggression',
                        'CB Rate',
                        'FB Rate',
                        'CDM Rate',
                        'CM Rate',
                        'CAM Rate',
                        'W Rate',
                        'ST Rate',
                        'URL'
                        ))
        for player in players:
            a_pen.writerow((player['rating'],
                            player['player_name'],
                            player['position'],
                            player['club'],
                            player['nation'],
                            player['league'],
                            player['skills'],
                            player['weak_foot'],
                            player['foot'],
                            player['height'],
                            player['weight'],
                            player['revision'],
                            player['def_wr'],
                            player['att_wr'],
                            player['traits'],
                            player['pace'],
                            player['acceleration'],
                            player['sprint_speed'],
                            player['shooting'],
                            player['positioning'],
                            player['finishing'],
                            player['shot_power'],
                            player['long_shots'],
                            player['volleys'],
                            player['penalties'],
                            player['passing'],
                            player['vision'],
                            player['crossing'],
                            player['fk_acc'],
                            player['short_passing'],
                            player['long_passing'],
                            player['curve'],
                            player['dribbling_m'],
                            player['agility'],
                            player['balance'],
                            player['reactions'],
                            player['ball_control'],
                            player['dribbling'],
                            player['composure'],
                            player['defending'],
                            player['interceptions'],
                            player['heading_accuracy'],
                            player['marking'],
                            player['standing_tackle'],
                            player['sliding_tackle'],
                            player['physicality'],
                            player['jumping'],
                            player['stamina'],
                            player['strength'],
                            player['aggression'],
                            player['best_cb'],
                            player['best_fb'],
                            player['best_cdm'],
                            player['best_cm'],
                            player['best_cam'],
                            player['best_w'],
                            player['best_st'],
                            player['url']
                            ))


players = fb_parse(base_url, headers)
files_writer(players)
print("Let's go !")
