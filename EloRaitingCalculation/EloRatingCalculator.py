from Match import Match
from Team import Team

class EloRatingCalculator():
    __k = 24

    def CalculateElo(self, match):
        if type(match) is not Match:
            raise TypeError('input must be a Match')

        WinExpectedHomeTeam = round(1 / ( 1 + 10 ** ((match.AwayTeam.EloRating - match.HomeTeam.EloRating) / 400 )), 2)
        WinExpectedAwayTeam = round(1 / ( 1 + 10 ** ((match.HomeTeam.EloRating - match.AwayTeam.EloRating) / 400 )), 2)

        print(WinExpectedHomeTeam)
        print(WinExpectedAwayTeam)

        if match.HomeScore > match.AwayScore:
            homeNewRating = match.HomeTeam.EloRating + (self.__k * (2 - WinExpectedHomeTeam))
            awayNewRating = match.AwayTeam.EloRating - (self.__k * (2 - WinExpectedAwayTeam))
        elif match.AwayScore > match.HomeScore:
            homeNewRating = match.HomeTeam.EloRating - (self.__k * (2 - WinExpectedHomeTeam))
            awayNewRating = match.AwayTeam.EloRating + (self.__k * (2 - WinExpectedAwayTeam))
        else:
            if match.HomeTeam.EloRating > match.AwayTeam.EloRating:
                homeNewRating = match.HomeTeam.EloRating + ((self.__k * (2 - WinExpectedHomeTeam))) / 2
                awayNewRating = match.AwayTeam.EloRating - ((self.__k * (2 - WinExpectedAwayTeam))) / 2
            elif match.AwayTeam.EloRating > match.HomeTeam.EloRating:
                homeNewRating = match.HomeTeam.EloRating - ((self.__k * (2 - WinExpectedHomeTeam))) / 2
                awayNewRating = match.AwayTeam.EloRating + ((self.__k * (2 - WinExpectedAwayTeam))) / 2
            else:
                homeNewRating = match.HomeTeam.EloRating
                awayNewRating = match.AwayTeam.EloRating

        if homeNewRating > 1000:
            homeNewRating = round(homeNewRating)
        else:
            homeNewRating = 1000

        if awayNewRating > 1000:
            awayNewRating = round(awayNewRating)
        else:
            awayNewRating = 1000

        print(f'{match.HomeTeam.Name} new Rating: {homeNewRating}')
        print(f'{match.AwayTeam.Name} new Rating: {awayNewRating}')

        return True


