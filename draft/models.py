from django.db import models

# Create your models here.
class Player(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    importMethod = models.CharField(max_length=20)
    bpId = models.IntegerField()
    mlbId = models.IntegerField()
    pos = models.CharField(max_length=3)

    def _getFullName(self):
        return self.firstName + ' ' + self.lastName

    fullName = property(_getFullName)
    
    def __unicode__(self):
        return self.firstName + ' ' + self.lastName + '(from ' + self.importMethod + ')'
    
class BatterYearLine(models.Model):
    player = models.ForeignKey(Player)
    label = models.CharField(max_length=30)
    yearLabel = models.CharField(max_length=15)
    age = models.IntegerField()
    team = models.CharField(max_length=4)
    league = models.CharField(max_length=3)
    atBats = models.IntegerField()
    hits = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    homeRuns = models.IntegerField()
    runs = models.IntegerField()
    rbi = models.IntegerField()
    walks = models.IntegerField()
    strikeouts = models.IntegerField()
    stolenBases = models.IntegerField()
    totalAvg = models.DecimalField(decimal_places=3, max_digits=4)
    vorp = models.DecimalField(decimal_places=1, max_digits=5)
    avg = models.DecimalField(decimal_places=3, max_digits=4)
    obp = models.DecimalField(decimal_places=3, max_digits=4)
    slg = models.DecimalField(decimal_places=3, max_digits=4)
    totalBases = models.IntegerField()

    def _getFullLabel(self):
        return self.yearLabel + ' ' + self.label

    fullLabel = property(_getFullLabel)
    
class PitcherYearLine(models.Model):
    player = models.ForeignKey(Player)
    label = models.CharField(max_length=30)
    yearLabel = models.CharField(max_length=15)
    age = models.IntegerField()
    team = models.CharField(max_length=4)
    league = models.CharField(max_length=3)
    inningsPitched = models.DecimalField(decimal_places=1, max_digits=5)
    era = models.DecimalField(decimal_places=2, max_digits=4)
    hitsAllowed = models.IntegerField()
    walksAllowed = models.IntegerField()
    strikeouts = models.IntegerField()
    wins = models.DecimalField(decimal_places=1, max_digits=3)
    saves = models.DecimalField(decimal_places=1, max_digits=3)
    fairRa = models.DecimalField(decimal_places=2, max_digits=4)
    warp = models.DecimalField(decimal_places=1, max_digits=3)
    games = models.DecimalField(decimal_places=1, max_digits=3)
    gamesStarted = models.DecimalField(decimal_places=1, max_digits=3)
    qualityStarts = models.DecimalField(decimal_places=1, max_digits=3)
    whip = models.DecimalField(decimal_places=3, max_digits=4)
    bb9 = models.DecimalField(decimal_places=1, max_digits=3)
    k9 = models.DecimalField(decimal_places=1, max_digits=3)
    kbbRatio = models.DecimalField(decimal_places=2, max_digits=4)

    def _getFullLabel(self):
        return self.yearLabel + ' ' + self.label

    fullLabel = property(_getFullLabel)
        
class League(models.Model):
    leagueType = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
class Team(models.Model):
    league = models.ForeignKey(League)
    teamName = models.CharField(max_length=50)
    managerName = models.CharField(max_length=50)

class DraftPick(models.Model):
    league = models.ForeignKey(League)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player)
    pick = models.IntegerField()