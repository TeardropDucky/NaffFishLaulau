from bs4 import BeautifulSoup, NavigableString
import requests
from datetime import datetime

from Match import Match
from Week import Week
from Season import Season

class ProFootballReference:
    __baseURL = 'https://www.pro-football-reference.com'

    __monthSwitch = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }

    def __init__(self, Teams):
        self.Teams = Teams

    def __findTeam(self, TeamName):
        for team in self.Teams:
            if team.AltTeamName is not None or team.AltHomeCity is not None:
                if TeamName == team.AltHomeCity + ' ' + team.TeamName:
                    return team
                elif TeamName == team.HomeCity + ' ' + team.AltTeamName:
                    return team
            if TeamName == team.Name:
                return team
        return None

    def __findTimeOfGame(self, Year, Date, Clock):
        month, day = Date.split(' ')
        month = self.__monthSwitch[month]
        hour, slicing = Clock.split(':')
        minute = slicing[:2]
        pmoram = slicing[2:]
        hour = int(hour)
        if pmoram == 'PM' and hour is not 12:
            hour = int(hour) + 12

        timeOfGame = datetime(Year, month, int(day), hour, int(minute), 0, 0)
        return timeOfGame

    def RetrieveSeason(self, Year):
        try:
            url = self.__baseURL + '/years/' + str(Year) + '/games.htm'
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            fullTable = soup.find_all('tbody')

            homeWins = 0
            awayWins = 0
            gameWeeks = []
            for i in range(1, 17):
                gameWeeks.append(Week(str(i), []))
            gameWeeks.append(Week('WildCard', []))
            gameWeeks.append(Week('Division', []))
            gameWeeks.append(Week('ConfChamp', []))
            gameWeeks.append(Week('SuperBowl', []))

            for content in fullTable[0].contents:
                if type(content) == NavigableString:
                    continue
                else:
                    # Home Team Won
                    if content.contents[5].text == '':
                        if content.contents[2].text == "Playoffs" or content.contents[2].text == "Date":
                            continue
                        homeTeam = self.__findTeam(content.contents[4].text)
                        homeScore = content.contents[8].text
                        awayTeam = self.__findTeam(content.contents[6].text)
                        awayScore = content.contents[9].text
                        boxscoreURL = self.__baseURL + content.contents[7].contents[0].attrs['href']
                        dateOfGame = self.__findTimeOfGame(Year, content.contents[2].text, content.contents[3].text)
                        weekOfGame = content.contents[0].text
                        homeWins += 1
                    #Away Team won
                    elif content.contents[5].text == '@':
                        homeTeam = self.__findTeam(content.contents[6].text)
                        homeScore = content.contents[9].text
                        awayTeam = self.__findTeam(content.contents[4].text)
                        awayScore = content.contents[8].text
                        boxscoreURL = self.__baseURL + content.contents[7].contents[0].attrs['href']
                        dateOfGame = self.__findTimeOfGame(Year, content.contents[2].text, content.contents[3].text)
                        weekOfGame = content.contents[0].text
                        awayWins += 1
                    #Superbowl
                    elif content.contents[5].text == 'N':
                        homeTeam = self.__findTeam(content.contents[4].text)
                        homeScore = content.contents[8].text
                        awayTeam = self.__findTeam(content.contents[6].text)
                        awayScore = content.contents[9].text
                        boxscoreURL = self.__baseURL + content.contents[7].contents[0].attrs['href']
                        dateOfGame = self.__findTimeOfGame(Year, content.contents[2].text, content.contents[3].text)
                        weekOfGame = content.contents[0].text
                    else:
                        continue

                    for week in gameWeeks:
                        if week.Week == weekOfGame:
                            week.Matches.append(Match(homeTeam, homeScore, awayTeam, awayScore, boxscoreURL, dateOfGame))
                            break

            season = Season(Year, gameWeeks, homeWins, awayWins)
        except Exception as e:
            print(e)
            season = None
        finally:
            return season

