# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BatterYearLine.totalAvg'
        db.add_column('draft_batteryearline', 'totalAvg', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BatterYearLine.totalAvg'
        db.delete_column('draft_batteryearline', 'totalAvg')


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
            'totalAvg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
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
