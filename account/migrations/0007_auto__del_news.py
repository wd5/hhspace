# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('account_news')


    def backwards(self, orm):
        
        # Adding model 'News'
        db.create_table('account_news', (
            ('subtitle', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['News'])


    models = {
        'account.audio': {
            'Meta': {'ordering': "['-timestamp', 'order']", 'object_name': 'Audio'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'audio': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'right_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['account.Singer']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'words_author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2000'})
        },
        'account.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Region']"})
        },
        'account.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.customuser': {
            'Meta': {'object_name': 'CustomUser', '_ormbases': ['auth.User']},
            'biography': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['account.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['account.Country']"}),
            'mood': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['account.Region']"}),
            'sex': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'account.direction': {
            'Meta': {'object_name': 'Direction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.photo': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.PhotoAlbum']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'visited': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'account.photoalbum': {
            'Meta': {'ordering': "['-date_updated']", 'object_name': 'PhotoAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Singer']"}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2011'})
        },
        'account.photocomment': {
            'Meta': {'ordering': "['-id']", 'object_name': 'PhotoComment'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': "'2011-06-05'", 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['account.Photo']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'singer_photocomment_set'", 'to': "orm['account.CustomUser']"})
        },
        'account.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.singer': {
            'Meta': {'object_name': 'Singer', '_ormbases': ['account.CustomUser']},
            'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['account.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'directions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Direction']", 'symmetrical': 'False'}),
            'featuring': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'index': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Style']", 'symmetrical': 'False'})
        },
        'account.singeralbum': {
            'Meta': {'ordering': "['date_update']", 'object_name': 'SingerAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Singer']"})
        },
        'account.style': {
            'Meta': {'ordering': "['name']", 'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.tracksingerablum': {
            'Meta': {'object_name': 'TrackSingerAblum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.SingerAlbum']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_by': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'perform_by': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'right_to': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'account.video': {
            'Meta': {'ordering': "['-timestamp', 'order']", 'object_name': 'Video'},
            'album': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'converted': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'director': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'flvvideo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['account.Singer']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2000'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['account']
