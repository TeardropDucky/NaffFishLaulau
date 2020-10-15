from Week import Week


class Season:

    def __init__(self, Year, Weeks, HomeWins, AwayWins):
        self.Weeks = Weeks
        self.Year = Year
        self.HomeWins = HomeWins
        self.AwayWins = AwayWins

    def __repr__(self):
        return f'Season({self.Year}, {self.Weeks}, {self.HomeWins}, {self.AwayWins})'
