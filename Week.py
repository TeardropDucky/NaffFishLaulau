from Match import  Match

class Week:

    def __init__(self, Week, Matches=None):
        if Matches is None:
            Matches = [Match]
        self.Matches = Matches
        self.Week = Week

    def __repr__(self):
        return f'{self.__class__.__name__}({self.Week},  {self.Matches})'

    @property
    def GamesPlayed(self):
        return len(self.Matches)

    def PrintTeamRatings(self):
        for match in self.Matches:
            print(match.HomeTeam)
            print(match.AwayTeam)