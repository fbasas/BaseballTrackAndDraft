# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Player'
        db.create_table('draft_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('importMethod', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bpId', self.gf('django.db.models.fields.IntegerField')()),
            ('mlbId', self.gf('django.db.models.fields.IntegerField')()),
            ('pos', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('draft', ['Player'])

        # Adding model 'BatterYearLine'
        db.create_table('draft_batteryearline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['draft.Player'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('yearLabel', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('team', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('atBats', self.gf('django.db.models.fields.IntegerField')()),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
            ('doubles', self.gf('django.db.models.fields.IntegerField')()),
            ('triples', self.gf('django.db.models.fields.IntegerField')()),
            ('homeRuns', self.gf('django.db.models.fields.IntegerField')()),
            ('runs', self.gf('django.db.models.fields.IntegerField')()),
            ('rbi', self.gf('django.db.models.fields.IntegerField')()),
            ('walks', self.gf('django.db.models.fields.IntegerField')()),
            ('strikeouts', self.gf('django.db.models.fields.IntegerField')()),
            ('stolenBases', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('draft', ['BatterYearLine'])

        # Adding model 'PitcherYearLine'
        db.create_table('draft_pitcheryearline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['draft.Player'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('yearLabel', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('inningsPitched', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('runsAllowed', self.gf('django.db.models.fields.IntegerField')()),
            ('earnedRunsAllowed', self.gf('django.db.models.fields.IntegerField')()),
            ('hitsAllowed', self.gf('django.db.models.fields.IntegerField')()),
            ('walksAllowed', self.gf('django.db.models.fields.IntegerField')()),
            ('strikeouts', self.gf('django.db.models.fields.IntegerField')()),
            ('wins', self.gf('django.db.models.fields.IntegerField')()),
            ('saves', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('draft', ['PitcherYearLine'])

        # Adding model 'League'
        db.create_table('draft_league', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('leagueType', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('draft', ['League'])

        # Adding model 'Team'
        db.create_table('draft_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['draft.League'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('draft', ['Team'])


    def backwards(self, orm):
        
        # Deleting model 'Player'
        db.delete_table('draft_player')

        # Deleting model 'BatterYearLine'
        db.delete_table('draft_batteryearline')

        # Deleting model 'PitcherYearLine'
        db.delete_table('draft_pitcheryearline')

        # Deleting model 'League'
        db.delete_table('draft_league')

        # Deleting model 'Team'
        db.delete_table('draft_team')


    models = {
        'draft.batteryearline': {
            'Meta': {'object_name': 'BatterYearLine'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'atBats': ('django.db.models.fields.IntegerField', [], {}),
            'doubles': ('django.db.models.fields.IntegerField', [], {}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'homeRuns': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['draft.Player']"}),
            'rbi': ('django.db.models.fields.IntegerField', [], {}),
            'runs': ('django.db.models.fields.IntegerField', [], {}),
            'stolenBases': ('django.db.models.fields.IntegerField', [], {}),
            'strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'triples': ('django.db.models.fields.IntegerField', [], {}),
            'walks': ('django.db.models.fields.IntegerField', [], {}),
            'yearLabel': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'draft.league': {
            'Meta': {'object_name': 'League'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leagueType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'draft.pitcheryearline': {
            'Meta': {'object_name': 'PitcherYearLine'},
            'earnedRunsAllowed': ('django.db.models.fields.IntegerField', [], {}),
            'hitsAllowed': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inningsPitched': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['draft.Player']"}),
            'runsAllowed': ('django.db.models.fields.IntegerField', [], {}),
            'saves': ('django.db.models.fields.IntegerField', [], {}),
            'strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'walksAllowed': ('django.db.models.fields.IntegerField', [], {}),
            'wins': ('django.db.models.fields.IntegerField', [], {}),
            'yearLabel': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'draft.player': {
            'Meta': {'object_name': 'Player'},
            'bpId': ('django.db.models.fields.IntegerField', [], {}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importMethod': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mlbId': ('django.db.models.fields.IntegerField', [], {}),
            'pos': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'draft.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['draft.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['draft']
