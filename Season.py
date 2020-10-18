from EloRaitingCalculation.EloRatingCalculator import EloRatingCalculator

from Week import Week
from Match import Match


class Season:

    def __init__(self, Year, Weeks, HomeWins, AwayWins):
        self.Weeks = Weeks
        self.Year = Year
        self.HomeWins = HomeWins
        self.AwayWins = AwayWins

    def __repr__(self):
        return f'Season({self.Year}, {self.Weeks}, {self.HomeWins}, {self.AwayWins})'

    def UpdateSeason(self):
        Elo = EloRatingCalculator()
        for week in self.Weeks:
            for match in week.Matches:
                Elo.CalculateElo(match)


