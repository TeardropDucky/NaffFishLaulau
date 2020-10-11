from DataRetrieving.ProFootballReference import ProFootballReference

from Team import Team

Arizona = Team("Arizona Cardinals")
Atalanta = Team("Atlanta Falcons")
Baltimore = Team("Baltimore Ravens")
Buffalo = Team("Buffalo Bills")
Carolina = Team("Carolina Panthers")
Chicago = Team('Chicago Bears')
Cincinnati = Team('Cincinnati Bengals')
Cleveland = Team('Cleveland Browns')
Dallas = Team('Dallas Cowboys')
Denver = Team('Denver Broncos')
Detroit = Team('Detroit Lions')
GreenBay = Team('Green Bay Packers')
Houston = Team('Houston Texans')
Indianapolis = Team('Indianapolis Colts')
Jacksonville = Team('Jacksonville Jaguars')
KansasCity= Team('Kansas City Chiefs')
LasVegas = Team('Las Vegas Raiders')
LosAngelesChargers = Team('Los Angeles Chargers')
LosAngelesRams = Team('Los Angeles Rams')
Miami= Team('Miami Dolphins')
Minnesota= Team('Minnesota Vikings')
NewEngland= Team('New England Patriots')
NewOrleans = Team('New Orleans Saints')
NewYorkGiants = Team('New York Giants')
NewYorkJets = Team('New York Jets')
Philadelphia = Team('Philadelphia Eagles')
Pittsburgh = Team('Pittsburgh Steelers')
SanFrancisco = Team("San Francisco 49ers")
Seattle = Team("Seattle Seahawks")
TampaBay = Team("Tampa Bay Buccaneers")
Tennessee = Team("Tennessee Titans")
Washington = Team("Washington Redskins")

Teams = [Arizona, Atalanta, Baltimore, Buffalo, Carolina, Chicago, Cincinnati, Cleveland, Dallas, Denver, Detroit,
         GreenBay, Houston, Indianapolis, Jacksonville, KansasCity, LasVegas, LosAngelesChargers, LosAngelesRams,
         Miami, Minnesota, NewEngland, NewOrleans, NewYorkGiants, NewYorkJets, Philadelphia, SanFrancisco, Seattle,
         TampaBay, Tennessee, Washington]



x = ProFootballReference(Teams)
print(x.RetrieveSeason(2002))