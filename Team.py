

class Team:

    def __init__(self, TeamName, EloRating=1000, HomeCity=None):
        self.TeamName = TeamName
        self.EloRating = EloRating
        self.HomeCity = HomeCity
        self.AltTeamName = ""
        self.AltHomeCity = ""

    def __repr__(self):
        return f'{self.__class__.__name__}({self.Name}, {self.EloRating})'

    @property
    def Name(self):
        return self.HomeCity + ' ' + self.TeamName

