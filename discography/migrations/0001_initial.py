# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'GroupAlbum'
        db.create_table('discography_groupalbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_creation', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 5, 15, 20, 56, 17, 715594), auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('date_update', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Group'])),
        ))
        db.send_create_signal('discography', ['GroupAlbum'])

        # Adding model 'SingerAlbum'
        db.create_table('discography_singeralbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_creation', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 5, 15, 20, 56, 17, 715594), auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('date_update', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('singer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Singer'])),
        ))
        db.send_create_signal('discography', ['SingerAlbum'])

        # Adding model 'TrackGroupAblum'
        db.create_table('discography_trackgroupablum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('music_by', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('perform_by', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('right_to', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discography.GroupAlbum'])),
        ))
        db.send_create_signal('discography', ['TrackGroupAblum'])

        # Adding model 'TrackSingerAblum'
        db.create_table('discography_tracksingerablum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('music_by', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('perform_by', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('right_to', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discography.SingerAlbum'])),
        ))
        db.send_create_signal('discography', ['TrackSingerAblum'])


    def backwards(self, orm):
        
        # Deleting model 'GroupAlbum'
        db.delete_table('discography_groupalbum')

        # Deleting model 'SingerAlbum'
        db.delete_table('discography_singeralbum')

        # Deleting model 'TrackGroupAblum'
        db.delete_table('discography_trackgroupablum')

        # Deleting model 'TrackSingerAblum'
        db.delete_table('discography_tracksingerablum')


    models = {
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
        'account.group': {
            'Meta': {'object_name': 'Group'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Country']"}),
            'date_created': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'featuring': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'leaders': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '255', 'blank': 'True'}),
            'mood': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Region']"}),
            'singers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Singer']", 'through': "orm['account.Membership']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Style']", 'symmetrical': 'False'})
        },
        'account.membership': {
            'Meta': {'object_name': 'Membership'},
            'date_joined': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_reason': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Singer']"})
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
        'account.style': {
            'Meta': {'ordering': "['name']", 'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        },
        'discography.groupalbum': {
            'Meta': {'object_name': 'GroupAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_creation': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 5, 15, 20, 56, 17, 715594)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'discography.singeralbum': {
            'Meta': {'object_name': 'SingerAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_creation': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 5, 15, 20, 56, 17, 715594)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Singer']"})
        },
        'discography.trackgroupablum': {
            'Meta': {'object_name': 'TrackGroupAblum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discography.GroupAlbum']"}),
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
        'discography.tracksingerablum': {
            'Meta': {'object_name': 'TrackSingerAblum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discography.SingerAlbum']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_by': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'perform_by': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'right_to': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['discography']
