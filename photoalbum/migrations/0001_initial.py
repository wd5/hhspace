# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Photoalbum'
        db.create_table('photoalbum_photoalbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('photoalbum', ['Photoalbum'])

        # Adding model 'Photo'
        db.create_table('photoalbum_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('visited', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoalbum.Photoalbum'])),
        ))
        db.send_create_signal('photoalbum', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'Photoalbum'
        db.delete_table('photoalbum_photoalbum')

        # Deleting model 'Photo'
        db.delete_table('photoalbum_photo')


    models = {
        'photoalbum.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photoalbum.Photoalbum']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'visited': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photoalbum.photoalbum': {
            'Meta': {'object_name': 'Photoalbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['photoalbum']
