# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Group'
        db.create_table('group_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_visit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Region'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.City'])),
            ('leaders', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=255, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 5, 31, 2, 36, 40, 179297), auto_now=True, blank=True)),
            ('featuring', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 5, 31, 2, 36, 40, 179410), auto_now=True, blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('group', ['Group'])

        # Adding M2M table for field directions on 'Group'
        db.create_table('group_group_directions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['group.group'], null=False)),
            ('direction', models.ForeignKey(orm['account.direction'], null=False))
        ))
        db.create_unique('group_group_directions', ['group_id', 'direction_id'])

        # Adding M2M table for field styles on 'Group'
        db.create_table('group_group_styles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['group.group'], null=False)),
            ('style', models.ForeignKey(orm['account.style'], null=False))
        ))
        db.create_unique('group_group_styles', ['group_id', 'style_id'])

        # Adding model 'Membership'
        db.create_table('group_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('singer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Singer'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.Group'])),
            ('date_joined', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('invite_reason', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
        ))
        db.send_create_signal('group', ['Membership'])

        # Adding model 'GroupAlbum'
        db.create_table('group_groupalbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.Group'])),
        ))
        db.send_create_signal('group', ['GroupAlbum'])

        # Adding model 'TrackGroupAblum'
        db.create_table('group_trackgroupablum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('music_by', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('perform_by', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('right_to', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.GroupAlbum'])),
        ))
        db.send_create_signal('group', ['TrackGroupAblum'])


    def backwards(self, orm):
        
        # Deleting model 'Group'
        db.delete_table('group_group')

        # Removing M2M table for field directions on 'Group'
        db.delete_table('group_group_directions')

        # Removing M2M table for field styles on 'Group'
        db.delete_table('group_group_styles')

        # Deleting model 'Membership'
        db.delete_table('group_membership')

        # Deleting model 'GroupAlbum'
        db.delete_table('group_groupalbum')

        # Deleting model 'TrackGroupAblum'
        db.delete_table('group_trackgroupablum')


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
        'group.group': {
            'Meta': {'object_name': 'Group'},
            'biography': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Country']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 31, 2, 36, 40, 179297)', 'auto_now': 'True', 'blank': 'True'}),
            'directions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Direction']", 'symmetrical': 'False'}),
            'featuring': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_visit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'leaders': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Region']"}),
            'singers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Singer']", 'through': "orm['group.Membership']", 'symmetrical': 'False'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Style']", 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 31, 2, 36, 40, 179410)', 'auto_now': 'True', 'blank': 'True'})
        },
        'group.groupalbum': {
            'Meta': {'object_name': 'GroupAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'group.membership': {
            'Meta': {'object_name': 'Membership'},
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_reason': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Singer']"})
        },
        'group.trackgroupablum': {
            'Meta': {'object_name': 'TrackGroupAblum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.GroupAlbum']"}),
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

    complete_apps = ['group']
