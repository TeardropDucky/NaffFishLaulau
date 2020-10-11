from bs4 import BeautifulSoup, NavigableString
import requests

from Match import Match
from Team import Team
from Week import Week
from Season import Season

class ProFootballReference:
    __baseURL = 'https://www.pro-football-reference.com'

    def __init__(self, Teams):
        self.Teams = Teams

    def __findTeam(self, TeamName):
        for team in self.Teams:
            if team.Name == TeamName:
                return team
        return None

    def RetrieveSeason(self, Year):
        try:
            url = self.__baseURL + '/years/' + str(Year) + '/games.htm'
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            fullTable = soup.find_all('tbody')

            homeWins = 0
            awayWins = 0
            weeks = { '1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : [], '9' : [],
                      '10' : [], '11' : [], '12' : [], '13' : [], '14' : [], '15' : [], '16' : [], '17' : [],
                      'WildCard' : [], 'Division' : [], 'ConfChamp' : [], 'SuperBowl' : []}

            for content in fullTable[0].contents:
                if type(content) == NavigableString:
                    continue
                else:
                    # Home Team Won
                    if content.contents[5].text == '':
                        if content.contents[2].text == "Playoffs" or content.contents[2].text == "Date":
                            continue
                        homeTeam = self.__findTeam(content.contents[4].text)
                        awayTeam = self.__findTeam(content.contents[6].text)
                        boxscoreURL = self.__baseURL + content.contents[7].contents[0].attrs['href']
                        weeks[content.contents[0].text].append(Match(homeTeam,
                                                                     content.contents[8].text,
                                                                     awayTeam,
                                                                     content.contents[9].text,
                                                                     boxscoreURL,
                                                                     content.contents[1].text,
                                                                     content.contents[2].text,
                                                                     content.contents[3].text)
                                                               )
                        homeWins += 1
                    #Away Team won
                    elif content.contents[5].text == '@':
                        homeTeam = self.__findTeam(content.contents[6].text)
                        awayTeam = self.__findTeam(content.contents[4].text)
                        boxscoreURL = self.__baseURL + content.contents[7].contents[0].attrs['href']
                        weeks[content.contents[0].text].append(Match(homeTeam,
                                                                     content.contents[9].text,
                                                                     awayTeam,
                                                                     content.contents[8].text,
                                                                     boxscoreURL,
                                                                     content.contents[1].text,
                                                                     content.contents[2].text,
                                                                     content.contents[3].text)
                                                               )
                        awayWins += 1
                    #Superbowl
                    elif content.contents[5].text == 'N':
                        homeTeam = self.__findTeam(content.contents[4].text)
                        awayTeam = self.__findTeam(content.contents[6].text)
                        boxscoreURL = self.__baseURL + content.contents[7].contents[0].attrs['href']
                        weeks[content.contents[0].text].append(Match(homeTeam,
                                                                     content.contents[8].text,
                                                                     awayTeam,
                                                                     content.contents[9].text,
                                                                     boxscoreURL,
                                                                     content.contents[1].text,
                                                                     content.contents[2].text,
                                                                     content.contents[3].text)
                                                               )
                    else:
                        continue

            print('Count home wins: ' + str(homeWins))
            print('Count way wins: ' + str(awayWins))

            season = Season(Year, weeks, homeWins, awayWins)
        except Exception as e:
            print(e)
            season = None
        finally:
            return season

