#This is a program to extract results from the recent valorant matches.

import requests
from bs4 import BeautifulSoup

url = "https://www.vlr.gg/matches/results"

#send http get request to the url and obtain the text contents in html_data variable
html_data = requests.get(url).text

#parse the html_data using beautifulsoup library and html5lib parsing algorithm
soup = BeautifulSoup(html_data, 'html5lib')

#find all the div tags containing the name of the team and score and put them in an iterable object named divs_list
divs_list = soup.find_all("div", class_="match-item-vs")

teams_list = []

scores_list = []

for div in divs_list:
    #find all the div tag containing the name of the team by acessing the child of each div tag in divs_list
    team_divs_list = div.find_all("div", class_="text-of")

    for team_div in team_divs_list:
        #extract the navigable sring(name of the team) from the div tag containing team name
        team_name = team_div.text
        #transform beautifulsoup string to python string
        team_name_str = str(team_name)
        # remove \t(tabs) and \n(newlines) from the team_str and store it in stripped_team_str
        stripped_team_str = team_name_str.strip()
        teams_list.append(stripped_team_str)

    #find all the div tag containing the score by acessing the child of each div tag in divs_list
    score_divs_list = div.find_all("div", class_="match-item-vs-team-score js-spoiler")

    for score_tag in score_divs_list:
        #extract the navigable sring(score) from the div tag containing score
        score = score_tag.string
        #transform beautifulsoup string to python string
        score_str = str(score)
        # remove \t(tabs) and \n(newlines) from the score_str and store it in stripped_score_str
        stripped_score_str = score_str.strip()
        scores_list.append(stripped_score_str)


#Display the results in a format like this: <team-1>  <score-1>  VS  <score-2>  <team-2>
for i, team in enumerate(teams_list):
    if i % 2 == 0:
        print(team, end="\t")
        print(scores_list[i], end="\t")
        print("VS", end="\t")
    else:
        print(scores_list[i], end="\t")
        print(team, end="\t")
        print("\n")



