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
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customuser.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customuser.Region'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customuser.City'])),
            ('leaders', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=255, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 7, 6, 23, 25, 19, 791830), auto_now=True, blank=True)),
            ('featuring', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 7, 6, 23, 25, 19, 791948), auto_now=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Online', max_length=50, blank=True)),
            ('mood', self.gf('django.db.models.fields.CharField')(default='\xd0\x9e\xd1\x82\xd0\xbf\xd0\xb0\xd0\xb4', max_length=50, blank=True)),
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
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('year', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.Group'])),
        ))
        db.send_create_signal('group', ['GroupAlbum'])

        # Adding model 'TrackGroupAblum'
        db.create_table('group_trackgroupablum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('music_by', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('perform_by', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('right_to', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2012)),
            ('duration', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.GroupAlbum'])),
        ))
        db.send_create_signal('group', ['TrackGroupAblum'])

        # Adding model 'PhotoAlbum'
        db.create_table('group_photoalbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2011)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.Group'])),
        ))
        db.send_create_signal('group', ['PhotoAlbum'])

        # Adding model 'Photo'
        db.create_table('group_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('visited', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group.PhotoAlbum'])),
        ))
        db.send_create_signal('group', ['Photo'])

        # Adding model 'PhotoComment'
        db.create_table('group_photocomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default='2011-07-06', auto_now=True, auto_now_add=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='group_photocomment_set', to=orm['customuser.CustomUser'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['group.Photo'])),
        ))
        db.send_create_signal('group', ['PhotoComment'])

        # Adding model 'Video'
        db.create_table('group_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100)),
            ('photo', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('flvideo', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('director', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2000)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('album', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('converted', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['group.Group'])),
        ))
        db.send_create_signal('group', ['Video'])

        # Adding model 'Audio'
        db.create_table('group_audio', (
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
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['group.Group'])),
        ))
        db.send_create_signal('group', ['Audio'])

        # Adding model 'BookmarkGroup'
        db.create_table('group_bookmarkgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='bookmarks_groups', to=orm['customuser.CustomUser'])),
            ('mark', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='mark_groups', to=orm['group.Group'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('group', ['BookmarkGroup'])


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

        # Deleting model 'PhotoAlbum'
        db.delete_table('group_photoalbum')

        # Deleting model 'Photo'
        db.delete_table('group_photo')

        # Deleting model 'PhotoComment'
        db.delete_table('group_photocomment')

        # Deleting model 'Video'
        db.delete_table('group_video')

        # Deleting model 'Audio'
        db.delete_table('group_audio')

        # Deleting model 'BookmarkGroup'
        db.delete_table('group_bookmarkgroup')


    models = {
        'account.direction': {
            'Meta': {'object_name': 'Direction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.singer': {
            'Meta': {'object_name': 'Singer', '_ormbases': ['customuser.CustomUser']},
            'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['customuser.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'directions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Direction']", 'symmetrical': 'False'}),
            'featuring': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'index': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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
        'customuser.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customuser.Region']"})
        },
        'customuser.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'customuser.customuser': {
            'Meta': {'object_name': 'CustomUser', '_ormbases': ['auth.User']},
            'biography': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['customuser.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['customuser.Country']"}),
            'mood': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\x9e\\xd1\\x82\\xd0\\xbf\\xd0\\xb0\\xd0\\xb4'", 'max_length': '50', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['customuser.Region']"}),
            'sex': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Online'", 'max_length': '50', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'customuser.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customuser.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'group.audio': {
            'Meta': {'ordering': "['-timestamp', 'order']", 'object_name': 'Audio'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'audio': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'right_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'words_author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2000'})
        },
        'group.bookmarkgroup': {
            'Meta': {'object_name': 'BookmarkGroup'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'mark_groups'", 'to': "orm['group.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'bookmarks_groups'", 'to': "orm['customuser.CustomUser']"})
        },
        'group.group': {
            'Meta': {'object_name': 'Group'},
            'biography': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customuser.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customuser.Country']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 7, 6, 23, 25, 19, 791830)', 'auto_now': 'True', 'blank': 'True'}),
            'directions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Direction']", 'symmetrical': 'False'}),
            'featuring': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_visit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'leaders': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '255', 'blank': 'True'}),
            'mood': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\x9e\\xd1\\x82\\xd0\\xbf\\xd0\\xb0\\xd0\\xb4'", 'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customuser.Region']"}),
            'singers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Singer']", 'through': "orm['group.Membership']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Online'", 'max_length': '50', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Style']", 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 7, 6, 23, 25, 19, 791948)', 'auto_now': 'True', 'blank': 'True'})
        },
        'group.groupalbum': {
            'Meta': {'ordering': "['date_update']", 'object_name': 'GroupAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'})
        },
        'group.membership': {
            'Meta': {'object_name': 'Membership'},
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_reason': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'singer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Singer']"})
        },
        'group.photo': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.PhotoAlbum']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'visited': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'group.photoalbum': {
            'Meta': {'ordering': "['-date_updated']", 'object_name': 'PhotoAlbum'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2011'})
        },
        'group.photocomment': {
            'Meta': {'ordering': "['-id']", 'object_name': 'PhotoComment'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': "'2011-07-06'", 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['group.Photo']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'group_photocomment_set'", 'to': "orm['customuser.CustomUser']"})
        },
        'group.trackgroupablum': {
            'Meta': {'object_name': 'TrackGroupAblum'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group.GroupAlbum']"}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'duration': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_by': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'perform_by': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'right_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2012'})
        },
        'group.video': {
            'Meta': {'ordering': "['-timestamp', 'order']", 'object_name': 'Video'},
            'album': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'converted': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'director': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'flvideo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['group.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2000'})
        }
    }

    complete_apps = ['group']
