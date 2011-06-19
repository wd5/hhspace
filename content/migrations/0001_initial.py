# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('content_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('content', ['News'])

        # Adding model 'Event'
        db.create_table('content_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('content', ['Event'])

        # Adding model 'Page'
        db.create_table('content_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('content', ['Page'])


    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('content_news')

        # Deleting model 'Event'
        db.delete_table('content_event')

        # Deleting model 'Page'
        db.delete_table('content_page')


    models = {
        'content.event': {
            'Meta': {'object_name': 'Event'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'content.news': {
            'Meta': {'object_name': 'News'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'content.page': {
            'Meta': {'object_name': 'Page'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['content']
