from random import choice
import time
from typing import List

from icecream import ic
import pandas as pd
import openpyxl
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from user_agents import ua

class SeleniumDriver():
    def __init__(self):
        self.opts = Options()
        self.service = Service(executable_path="geckodriver.exe")
    
    def set_options(self):
        self.opts.add_argument("--headless")
        # self.opts.add_argument("--width=800")
        # self.opts.add_argument("--height=600")
        self.opts.set_preference("general.useragent.override", choice(ua))

    def get_driver(self):
        self.set_options()
        self.driver = webdriver.Firefox(service=self.service, options=self.opts)
        return self.driver


def get_urls_list(base_url: str, version: str) -> List[str]: 
    driver = SeleniumDriver().get_driver()
    total_urls = []
    page = 0

    while True:
        time.sleep(1)
        driver.get(base_url+f"{page}&release={version}")
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="pagination"]//div[contains(@class, "next")]')))

        players_url_list = driver.find_elements(By.XPATH, '//table[contains(@class, "playersearchresults")]//td[@class="face"]//a')
        for player_url in players_url_list:
            full_url = player_url.get_attribute("href")
            if full_url not in total_urls:
                total_urls.append(full_url)

        next_page_flag = driver.find_element(By.XPATH, '//div[@class="pagination"]//div[contains(@class, "next")]').text
        # if page == 1:
        #     break
        if next_page_flag != "Next":
            break
        page += 1

    driver.quit()
    return total_urls


def get_players_stats(total_urls):
    driver = SeleniumDriver().get_driver()
    players = [""] * len(total_urls)
    for idx, url in enumerate(tqdm(total_urls)):
        try:
            driver.get(url)
            time.sleep(2)

            rating = driver.find_element(By.XPATH, '//div[contains(@class, "rating")]').text
            name = driver.find_element(By.XPATH, '//h1/div[1]').text
            revision_club_nation_league = driver.find_element(By.XPATH, '//h1/div[2]').text.split(" | ")
            if len(revision_club_nation_league) == 4:
                revision, nation, club, league = revision_club_nation_league
            else:
                revision, nation, league = revision_club_nation_league
                club = "Heroes"
            position = driver.find_element(By.XPATH, '//div[contains(@class, "position")]').text

            pace = int(driver.find_element(By.XPATH, '//div[contains(@class, "att1bar")]').text)
            acceleration = int(driver.find_element(By.XPATH, '//div[contains(@class, "accelerationstat")]').text)
            sprint_speed = int(driver.find_element(By.XPATH, '//div[contains(@class, "sprintspeedstat")]').text)
            shooting = int(driver.find_element(By.XPATH, '//div[contains(@class, "att2bar")]').text)
            positioning = int(driver.find_element(By.XPATH, '//div[contains(@class, "positioningstat")]').text)
            finishing = int(driver.find_element(By.XPATH, '//div[contains(@class, "finishingstat")]').text)
            shot_power = int(driver.find_element(By.XPATH, '//div[contains(@class, "shotpowerstat")]').text)
            long_shots = int(driver.find_element(By.XPATH, '//div[contains(@class, "longshotstat")]').text)
            volleys = int(driver.find_element(By.XPATH, '//div[contains(@class, "volleysstat")]').text)
            penalties = int(driver.find_element(By.XPATH, '//div[contains(@class, "penaltiesstat")]').text)
            passing = int(driver.find_element(By.XPATH, '//div[contains(@class, "att3bar")]').text)
            vision = int(driver.find_element(By.XPATH, '//div[contains(@class, "visionstat")]').text)
            crossing = int(driver.find_element(By.XPATH, '//div[contains(@class, "crossingstat")]').text)
            fk_acc = int(driver.find_element(By.XPATH, '//div[contains(@class, "fkaccstat")]').text)
            short_passing = int(driver.find_element(By.XPATH, '//div[contains(@class, "shortpassstat")]').text)
            long_passing = int(driver.find_element(By.XPATH, '//div[contains(@class, "longpassstat")]').text)
            curve = int(driver.find_element(By.XPATH, '//div[contains(@class, "curvestat")]').text)
            dribbling_m = int(driver.find_element(By.XPATH, '//div[contains(@class, "att4bar")]').text)
            agility = int(driver.find_element(By.XPATH, '//div[contains(@class, "agilitystat")]').text)
            balance = int(driver.find_element(By.XPATH, '//div[contains(@class, "balancestat")]').text)
            reactions = int(driver.find_element(By.XPATH, '//div[contains(@class, "reactionsstat")]').text)
            ball_control = int(driver.find_element(By.XPATH, '//div[contains(@class, "ballcontrolstat")]').text)
            dribbling = int(driver.find_element(By.XPATH, '//div[contains(@class, "dribblingstat")]').text)
            composure = int(driver.find_element(By.XPATH, '//div[contains(@class, "composurestat")]').text)
            defending = int(driver.find_element(By.XPATH, '//div[contains(@class, "att5bar")]').text)
            interceptions = int(driver.find_element(By.XPATH, '//div[contains(@class, "tactawarestat")]').text)
            heading_accuracy = int(driver.find_element(By.XPATH, '//div[contains(@class, "headingaccstat")]').text)
            marking = int(driver.find_element(By.XPATH, '//div[contains(@class, "markingstat")]').text)
            standing_tackle = int(driver.find_element(By.XPATH, '//div[contains(@class, "standingtacklestat")]').text)
            sliding_tackle = int(driver.find_element(By.XPATH, '//div[contains(@class, "slidetacklestat")]').text)
            physicality = int(driver.find_element(By.XPATH, '//div[contains(@class, "att6bar")]').text)
            jumping = int(driver.find_element(By.XPATH, '//div[contains(@class, "jumpingstat")]').text)
            stamina = int(driver.find_element(By.XPATH, '//div[contains(@class, "staminastat")]').text)
            strength = int(driver.find_element(By.XPATH, '//div[contains(@class, "strengthstat")]').text)
            aggression = int(driver.find_element(By.XPATH, '//div[contains(@class, "aggressionstat")]').text)
            total_stats = int(driver.find_element(By.XPATH, '//span[contains(@class, "totalstatsdata")]').text.replace(",", ""))

            skills = int(driver.find_element(By.XPATH, '(//p[contains(@class, "ppskills")])[1]').text.strip())
            weak_foot = int(driver.find_element(By.XPATH, '(//p[contains(@class, "ppskills")])[2]').text.strip())
            foot = driver.find_element(By.XPATH, '(//p[@class="ppdb-d"])[5]').text.strip()
            height = int(driver.find_element(By.XPATH, '(//p[@class="ppdb-l"])[4]').text.strip().split("CM")[0])
            weight = int(driver.find_element(By.XPATH, '(//p[@class="ppdb-d"])[3]').text.strip().split("KG")[0])
            att_wr, def_wr = driver.find_element(By.XPATH, '(//p[@class="ppdb-d"])[4]').text.strip().split("/")
            traits = driver.find_element(By.XPATH, '//div[contains(text(), "Traits: ")]').text.replace("Traits: ", "")
            #FIXME возможно необходимо будет скорректировать индекс для новых рынков
            price_range = driver.find_element(By.XPATH, '(//div[@class="pricerange"])[3]').text.replace("PR: ", "")

            min_price, max_price = map(int, price_range.replace(",", "").split(" - "))

            att_wr_rate = 0
            if att_wr == 'HIGH':
                att_wr_rate = 1
            elif att_wr == 'MED':
                att_wr_rate = 0.66
            else:
                att_wr_rate = 0.33

            def_wr_rate = 0
            if def_wr == 'HIGH':
                def_wr_rate = 1
            elif def_wr == 'MED':
                def_wr_rate = 0.66
            else:
                def_wr_rate = 0.33
            skill_rate = round(skills * 0.2, 1)
            weak_foot_rate = round(weak_foot * 0.2, 1)

            players[idx] = {
                'rating': rating,
                'player_name': name,
                'position': position,
                'club': club,
                'nation': nation,
                'league': league,
                'skills': skill_rate,
                'weak_foot': weak_foot_rate,
                'foot': foot,
                'height': height / 100,
                'weight': weight,
                'revision': revision,
                'def_wr': def_wr_rate,
                'att_wr': att_wr_rate,
                'traits': traits,
                'min_price': min_price,
                'max_price': max_price,
                'pace': pace,
                'acceleration': acceleration,
                'sprint_speed': sprint_speed,
                'shooting': shooting,
                'positioning': positioning,
                'finishing': finishing,
                'shot_power': shot_power,
                'long_shots': long_shots,
                'volleys': volleys,
                'penalties': penalties,
                'passing': passing,
                'vision': vision,
                'crossing': crossing,
                'fk_acc': fk_acc,
                'short_passing': short_passing,
                'long_passing': long_passing,
                'curve': curve,
                'dribbling_m': dribbling_m,
                'agility': agility,
                'balance': balance,
                'reactions': reactions,
                'ball_control': ball_control,
                'dribbling': dribbling,
                'composure': composure,
                'defending': defending,
                'interceptions': interceptions,
                'heading_accuracy': heading_accuracy,
                'marking': marking,
                'standing_tackle': standing_tackle,
                'sliding_tackle': sliding_tackle,
                'physicality': physicality,
                'jumping': jumping,
                'stamina': stamina,
                'strength': strength,
                'aggression': aggression,
                'total_stats': total_stats,
                'url': url,
            }
        except Exception as exc:
            print(f'error in {url}, exc: {exc}')
            pass
    driver.quit()
    return players

def add_analytic_variables(df):
    df["best_cb"] = (df["sprint_speed"]*2 + df["interceptions"] + df["marking"]*3 + 
                     df["standing_tackle"]*2 + df["jumping"] + df["strength"] + 
                     df["agility"] + df["balance"] + df["reactions"] + 
                     df["height"]*75 + df["heading_accuracy"] + df["aggression"]*2)
    max_best_cb = df["best_cb"].max()
    df["%_best_cb"] = df["best_cb"].apply(lambda x: x/max_best_cb)

    df["best_fb"] = (df["sprint_speed"]*5 + df["positioning"] + df["finishing"] + 
                     df["crossing"] + df["long_passing"] + df["agility"] + 
                     df["balance"] + df["standing_tackle"]*2 + df["marking"]*2 + 
                     df["interceptions"]*2 + df["stamina"] + df["weak_foot"]*50)
    max_best_fb = df["best_fb"].max()
    df["%_best_fb"] = df["best_fb"].apply(lambda x: x/max_best_fb)

    df["best_cdm"] = (df["sprint_speed"]*1.5 + df["shot_power"] + df["long_shots"] + 
                      df["short_passing"] + df["interceptions"]*2 + df["marking"]*3 + 
                      df["standing_tackle"]*2 + df["strength"] + df["aggression"] + 
                      df["height"]*75)
    max_best_cdm = df["best_cdm"].max()
    df["%_best_cdm"] = df["best_cdm"].apply(lambda x: x/max_best_cdm)

    df["best_cm"] = (df["def_wr"]*50 + df["att_wr"]*50 + df["sprint_speed"]*2.5 + 
                     df["shot_power"]*2 + df["long_shots"]*2 + df["vision"]*3 + 
                     df["short_passing"]*3 + df["long_passing"]*3 + df["curve"] + 
                     df["agility"] + df["balance"] + df["dribbling"] + 
                     df["ball_control"] + df["stamina"] + df["weak_foot"]*50 + 
                     df["interceptions"])
    max_best_cm = df["best_cm"].max()
    df["%_best_cm"] = df["best_cm"].apply(lambda x: x/max_best_cm)

    df["best_cam"] = (df["skills"]*50 + df["weak_foot"]*50 + df["sprint_speed"]*4 + 
                      df["positioning"] + df["finishing"] + df["vision"]*2 + 
                      df["crossing"]*2 + df["short_passing"]*2 + df["long_passing"]*2 + 
                      df["curve"] + df["agility"]*1.5 + df["balance"]*1.5 + 
                      df["reactions"]*1.5 + df["ball_control"]*1.5 + df["dribbling"]*1.5 + 
                      df["composure"])
    max_best_cam = df["best_cam"].max()
    df["%_best_cam"] = df["best_cam"].apply(lambda x: x/max_best_cam)

    df["best_w"] = (df["sprint_speed"]*5 + df["positioning"]*2 + df["finishing"]*2 + 
                    df["crossing"] + df["long_passing"]*2 + df["curve"]*2 + 
                    df["weak_foot"]*50 + df["skills"]*50 + df["strength"]*2 + 
                    df["composure"] + df["agility"]*1.5 + df["balance"]*1.5 + 
                    df["reactions"]*1.5 + df["ball_control"]*1.5 + df["dribbling"]*1.5)
    max_best_w = df["best_w"].max()
    df["%_best_w"] = df["best_w"].apply(lambda x: x/max_best_w)


    df["best_st"] = (df["sprint_speed"]*2 + df["positioning"]*2 + df["finishing"]*2 + 
                    df["composure"] + df["agility"] + df["balance"] + 
                    df["skills"]*50 + df["weak_foot"]*50)
    max_best_st = df["best_st"].max()
    df["%_best_st"] = df["best_st"].apply(lambda x: x/max_best_st)

    df["best_heading"] = (df["height"]*100 + df["heading_accuracy"] + df["jumping"])
    max_best_heading = df["best_heading"].max()
    df["%_best_heading"] = df["best_heading"].apply(lambda x: x/max_best_heading)


if __name__ == "__main__":
    base_url = 'https://www.futwiz.com/en/fifa22/players?page='
    total_url_list = []
    versions = ["icons", "nifgold"]

    for version in tqdm(versions):
        current_url_list = get_urls_list(base_url, version)
        total_url_list.extend(current_url_list)

    players_stats = get_players_stats(total_url_list)
    df = pd.DataFrame(players_stats)
    df.to_csv("dbs/test_backup.csv", index=False)
    # df = pd.read_csv("dbs/test_backup.csv")
    df = df[df["position"] != "GK"]
    df_without_icons = df[df["club"] != "Icons"]

    add_analytic_variables(df)
    add_analytic_variables(df_without_icons)

    df.to_excel("dbs/test_db.xlsx", index=False)
    df.to_csv("dbs/test_db.csv", index=False)
    df_without_icons.to_excel("dbs/test_db_without_icons.xlsx", index=False)
    df_without_icons.to_csv("dbs/test_db_without_icons.csv", index=False)
