from django.db import models

# Create your models here.
class Player(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    importMethod = models.CharField(max_length=20)
    bpId = models.IntegerField(null=True)
    mlbId = models.IntegerField(null=True)
    pos = models.CharField(max_length=3)
    thr = models.CharField(max_length=15, null=True)
    isStarter =  models.BooleanField()
    curTeam = models.CharField(max_length=4)

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
    league = models.CharField(max_length=3, null=True)
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
    totalBases = models.IntegerField(null=True)
    mmCode = models.CharField(max_length=12, null=True)
    dlDays = models.IntegerField(null=True)
    dollarValue = models.IntegerField(null=True)
    bbRatio = models.IntegerField(null=True)
    eye = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    contactRatio = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    px = models.IntegerField(null=True)
    groundBallRatio = models.IntegerField(null=True)
    lineDriveRatio = models.IntegerField(null=True)
    flyBallRatio = models.IntegerField(null=True)
    xba = models.DecimalField(decimal_places=3, max_digits=4, null=True)
    bpv = models.IntegerField(null=True)

    def _getFullLabel(self):
        return self.yearLabel + ' ' + self.label

    fullLabel = property(_getFullLabel)
    
class PitcherYearLine(models.Model):
    player = models.ForeignKey(Player)
    label = models.CharField(max_length=30)
    yearLabel = models.CharField(max_length=15)
    age = models.IntegerField()
    team = models.CharField(max_length=4)
    league = models.CharField(max_length=3, null=True)
    inningsPitched = models.DecimalField(decimal_places=1, max_digits=5)
    era = models.DecimalField(decimal_places=2, max_digits=4)
    hitsAllowed = models.IntegerField()
    walksAllowed = models.IntegerField()
    strikeouts = models.IntegerField()
    wins = models.DecimalField(decimal_places=1, max_digits=3)
    saves = models.DecimalField(decimal_places=1, max_digits=3)
    fairRa = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    warp = models.DecimalField(decimal_places=1, max_digits=3, null=True)
    games = models.DecimalField(decimal_places=1, max_digits=3)
    gamesStarted = models.DecimalField(decimal_places=1, max_digits=3, null=True)
    qualityStarts = models.DecimalField(decimal_places=1, max_digits=3)
    whip = models.DecimalField(decimal_places=3, max_digits=4)
    bb9 = models.DecimalField(decimal_places=1, max_digits=3)
    k9 = models.DecimalField(decimal_places=1, max_digits=3)
    kbbRatio = models.DecimalField(decimal_places=2, max_digits=4)
    mmCode = models.CharField(max_length=12, null=True)
    dlDays = models.IntegerField(null=True)
    xera = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    dollarValue = models.IntegerField(null=True)
    groundBallRatio = models.IntegerField(null=True)
    lineDriveRatio = models.IntegerField(null=True)
    flyBallRatio = models.IntegerField(null=True)
    hitRatio = models.IntegerField(null=True)
    bpv = models.IntegerField(null=True)

    def _getFullLabel(self):
        return self.yearLabel + ' ' + self.label

    fullLabel = property(_getFullLabel)
        
class League(models.Model):
    leagueType = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
    
class Team(models.Model):
    league = models.ForeignKey(League)
    teamName = models.CharField(max_length=50)
    managerName = models.CharField(max_length=50)
    draftPosition = models.IntegerField()

    def __unicode__(self):
        return self.teamName + '(' + self.league.name + ') #' + str(self.draftPosition)

    def _fullName(self):
        return self.teamName + ' (' + self.managerName + ')'

    fullName = property(_fullName)

class DraftPick(models.Model):
    league = models.ForeignKey(League)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player)
    pick = models.IntegerField()

    def __unicode__(self):
        return self.player.fullName + ' (#' + str(self.pick) + ') ' + self.team.teamName + ' (' + self.league.name + ')'