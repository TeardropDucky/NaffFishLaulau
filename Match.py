from Team import Team

class Match:

    def __init__(self, HomeTeam, HomeScore, AwayTeam, AwayScore, BoxScore, Day, Date, Time):
        self.HomeTeam = HomeTeam
        self.HomeScore = HomeScore

        self.AwayTeam = AwayTeam
        self.AwayScore = AwayScore

        self.BoxScore = BoxScore
        self.Day = Day
        self.Date = Date
        self.Time = Time