# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Audio.Singer'
        db.delete_column('audio_audio', 'Singer_id')


    def backwards(self, orm):
        
        # Adding field 'Audio.Singer'
        db.add_column('audio_audio', 'Singer', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['account.Singer']), keep_default=False)


    models = {
        'audio.audio': {
            'Meta': {'ordering': "['-timestamp', 'order']", 'object_name': 'Audio'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'audio': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'right_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'words_author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2000'})
        }
    }

    complete_apps = ['audio']
