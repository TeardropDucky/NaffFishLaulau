from datetime import datetime

from Team import Team

class Match:

    def __init__(self, HomeTeam, HomeScore, AwayTeam, AwayScore, BoxScore, GameDate):
        self.HomeTeam = HomeTeam
        self.HomeScore = HomeScore

        self.AwayTeam = AwayTeam
        self.AwayScore = AwayScore

        self.BoxScore = BoxScore
        self.GameDate = GameDate

    def __repr__(self):
        return f'{self.__class__.__name__}({self.HomeTeam}, {self.HomeScore}, {self.AwayTeam}, {self.AwayScore}, {self.GameDate})'

