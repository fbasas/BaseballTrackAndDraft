# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BatterYearLine.avg'
        db.add_column('draft_batteryearline', 'avg', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3), keep_default=False)

        # Adding field 'BatterYearLine.obp'
        db.add_column('draft_batteryearline', 'obp', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3), keep_default=False)

        # Adding field 'BatterYearLine.slg'
        db.add_column('draft_batteryearline', 'slg', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3), keep_default=False)

        # Adding field 'BatterYearLine.totalBases'
        db.add_column('draft_batteryearline', 'totalBases', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'PitcherYearLine.whip'
        db.add_column('draft_pitcheryearline', 'whip', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3), keep_default=False)

        # Adding field 'PitcherYearLine.bb9'
        db.add_column('draft_pitcheryearline', 'bb9', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=3, decimal_places=1), keep_default=False)

        # Adding field 'PitcherYearLine.k9'
        db.add_column('draft_pitcheryearline', 'k9', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=3, decimal_places=1), keep_default=False)

        # Adding field 'PitcherYearLine.kbbRatio'
        db.add_column('draft_pitcheryearline', 'kbbRatio', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=2), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BatterYearLine.avg'
        db.delete_column('draft_batteryearline', 'avg')

        # Deleting field 'BatterYearLine.obp'
        db.delete_column('draft_batteryearline', 'obp')

        # Deleting field 'BatterYearLine.slg'
        db.delete_column('draft_batteryearline', 'slg')

        # Deleting field 'BatterYearLine.totalBases'
        db.delete_column('draft_batteryearline', 'totalBases')

        # Deleting field 'PitcherYearLine.whip'
        db.delete_column('draft_pitcheryearline', 'whip')

        # Deleting field 'PitcherYearLine.bb9'
        db.delete_column('draft_pitcheryearline', 'bb9')

        # Deleting field 'PitcherYearLine.k9'
        db.delete_column('draft_pitcheryearline', 'k9')

        # Deleting field 'PitcherYearLine.kbbRatio'
        db.delete_column('draft_pitcheryearline', 'kbbRatio')


    models = {
        'draft.batteryearline': {
            'Meta': {'object_name': 'BatterYearLine'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'atBats': ('django.db.models.fields.IntegerField', [], {}),
            'avg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'doubles': ('django.db.models.fields.IntegerField', [], {}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'homeRuns': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'league': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'obp': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['draft.Player']"}),
            'rbi': ('django.db.models.fields.IntegerField', [], {}),
            'runs': ('django.db.models.fields.IntegerField', [], {}),
            'slg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'stolenBases': ('django.db.models.fields.IntegerField', [], {}),
            'strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'totalAvg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'totalBases': ('django.db.models.fields.IntegerField', [], {}),
            'triples': ('django.db.models.fields.IntegerField', [], {}),
            'vorp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
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
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'bb9': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'era': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'fairRa': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'games': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'gamesStarted': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'hitsAllowed': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inningsPitched': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'k9': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'kbbRatio': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'league': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['draft.Player']"}),
            'qualityStarts': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'saves': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'strikeouts': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'walksAllowed': ('django.db.models.fields.IntegerField', [], {}),
            'warp': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'whip': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'wins': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
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
