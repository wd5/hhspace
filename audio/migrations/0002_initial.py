# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Audio'
        db.create_table('audio_audio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('music_author', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('words_author', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2000)),
            ('right_to', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('audio', ['Audio'])


    def backwards(self, orm):
        
        # Deleting model 'Audio'
        db.delete_table('audio_audio')


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
