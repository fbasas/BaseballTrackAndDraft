from django.db import models

# Create your models here.
class Player(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    importMethod = models.CharField(max_length=20)
    bpId = models.IntegerField()
    mlbId = models.IntegerField()
    pos = models.CharField(max_length=3)
    
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

    def _getAvg(self):
        return float(self.hits) / float(self.atBats)

    avg = property(_getAvg)

    def _getObp(self):
        return float(self.walks + self.hits) / float(self.atBats + self.walks)

    obp = property(_getObp)

    def _getTotalBases(self):
        return self.hits + self.doubles + 2 * self.triples + 3 * self.homeRuns

    totalBases = property(_getTotalBases)

    def _getSlg(self):
        return float(self._getTotalBases()) / float(self.atBats)

    slg = property(_getSlg)

    def _getFullLabel(self):
        return self.yearLabel + ' ' + self.label;

    fullLabel = property(_getFullLabel)
    
class PitcherYearLine(models.Model):
    player = models.ForeignKey(Player)
    label = models.CharField(max_length=30)
    yearLabel = models.CharField(max_length=15)
    inningsPitched = models.DecimalField(decimal_places=1, max_digits=5)
    runsAllowed = models.IntegerField()
    earnedRunsAllowed = models.IntegerField()
    hitsAllowed = models.IntegerField()
    walksAllowed = models.IntegerField()
    strikeouts = models.IntegerField()
    wins = models.IntegerField()
    saves = models.IntegerField()
        
class League(models.Model):
    leagueType = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
class Team(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=50)