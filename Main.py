from DataRetrieving.ProFootballReference import ProFootballReference
from EloRaitingCalculation.EloRatingCalculator import EloRatingCalculator

from Team import Team
from Match import Match



Arizona = Team("Cardinals", 1000, "Arizona")
Atalanta = Team("Falcons", 1000, "Atlanta")
Baltimore = Team("Ravens", 1000, "Baltimore")
Buffalo = Team("Bills", 1000, "Buffalo")
Carolina = Team("Panthers", 1000, "Carolina")
Chicago = Team('Bears', 1000, 'Chicago')
Cincinnati = Team('Bengals', 1000, 'Cincinnati')
Cleveland = Team('Browns', 1000, 'Cleveland')
Dallas = Team('Cowboys', 1000, 'Dallas')
Denver = Team('Broncos', 1000, 'Denver')
Detroit = Team('Lions', 1000, 'Detroit')
GreenBay = Team('Packers', 1000, 'Green Bay')
Houston = Team('Texans', 1000, 'Houston')
Indianapolis = Team('Colts', 1000, 'Indianapolis')
Jacksonville = Team('Jaguars', 1000, 'Jacksonville')
KansasCity= Team('Chiefs', 1000, 'Kansas City')

LasVegas = Team('Raiders', 1000, 'Las Vegas')
LasVegas.HomeCity = "Oakland"

LosAngelesChargers = Team('Chargers', 1000, 'Los Angeles')
LosAngelesChargers.HomeCity = "San Diego"

LosAngelesRams = Team('Rams', 1000, 'Los Angeles')
LosAngelesRams.HomeCity = "St. Louis"

Miami= Team('Dolphins', 1000, 'Miami')
Minnesota= Team('Vikings', 1000, 'Minnesota')
NewEngland= Team('Patriots', 1000, 'New England')
NewOrleans = Team('Saints', 1000, 'New Orleans')
NewYorkGiants = Team('Giants', 1000, 'New York')
NewYorkJets = Team('Jets', 1000, 'New York')
Philadelphia = Team('Eagles', 1000, 'Philadelphia')
Pittsburgh = Team('Steelers', 1000, 'Pittsburgh')
SanFrancisco = Team("49ers", 1000, 'San Francisco')
Seattle = Team("Seahawks", 1000, 'Seattle')
TampaBay = Team("Buccaneers", 1000, 'Tampa Bay')
Tennessee = Team("Titans", 1000, 'Tennessee')

Washington = Team("Redskins", 1000, 'Washington')
Washington.AltTeamName = "Football Team"

Teams = [Arizona, Atalanta, Baltimore, Buffalo, Carolina, Chicago, Cincinnati, Cleveland, Dallas, Denver, Detroit,
         GreenBay, Houston, Indianapolis, Jacksonville, KansasCity, LasVegas, LosAngelesChargers, LosAngelesRams,
         Miami, Minnesota, NewEngland, NewOrleans, NewYorkGiants, NewYorkJets, Philadelphia, Pittsburgh, SanFrancisco,
         Seattle, TampaBay, Tennessee, Washington]




x = ProFootballReference(Teams)
season = x.RetrieveSeason(2002)
print(season)
for week in season.Weeks:
    if week.Week == 'SuperBowl':
        superBowl = week.Matches[0]
print(season.Weeks[0])
print(f'SuperBowl: {superBowl}')

Seattle.EloRating = 1000
testMatch = Match(Seattle, 10, Baltimore, 10, None, None)
season.Weeks[0].PrintTeamRatings()

R = EloRatingCalculator()
R.CalculateElo(testMatch)
R.CalculateElo(superBowl)
