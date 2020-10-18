

class Team:

    def __init__(self, TeamName, EloRating=1000, HomeCity=None):
        self.TeamName = TeamName
        self.EloRating = EloRating
        self.HomeCity = HomeCity
        self.AltTeamName = ""
        self.AltHomeCity = ""
        self.AvgPointDifferenceH = 0
        self.AvgPointDifferenceA = 0

    def __repr__(self):
        return f'{self.__class__.__name__}({self.Name}, {self.EloRating})'

    @property
    def Name(self):
        return self.HomeCity + ' ' + self.TeamName

    @property
    def AvgPointDifference(self):
        return round((self.AvgPointDifferenceH + self.AvgPointDifferenceA) / 2, 2)