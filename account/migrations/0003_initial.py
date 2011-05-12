# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Direction'
        db.create_table('account_direction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['Direction'])

        # Adding model 'Style'
        db.create_table('account_style', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['Style'])

        # Adding model 'Country'
        db.create_table('account_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['Country'])

        # Adding model 'Region'
        db.create_table('account_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Country'])),
        ))
        db.send_create_signal('account', ['Region'])

        # Adding model 'City'
        db.create_table('account_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Region'])),
        ))
        db.send_create_signal('account', ['City'])

        # Adding model 'Category'
        db.create_table('account_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['Category'])

        # Adding model 'CustomUser'
        db.create_table('account_customuser', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['account.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['account.Region'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['account.City'])),
            ('sex', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('mood', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(default='', max_length=100, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('account', ['CustomUser'])

        # Adding model 'Singer'
        db.create_table('account_singer', (
            ('customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.CustomUser'], unique=True, primary_key=True)),
            ('featuring', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('index', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('account', ['Singer'])

        # Adding M2M table for field directions on 'Singer'
        db.create_table('account_singer_directions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('singer', models.ForeignKey(orm['account.singer'], null=False)),
            ('direction', models.ForeignKey(orm['account.direction'], null=False))
        ))
        db.create_unique('account_singer_directions', ['singer_id', 'direction_id'])

        # Adding M2M table for field styles on 'Singer'
        db.create_table('account_singer_styles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('singer', models.ForeignKey(orm['account.singer'], null=False)),
            ('style', models.ForeignKey(orm['account.style'], null=False))
        ))
        db.create_unique('account_singer_styles', ['singer_id', 'style_id'])

        # Adding model 'Group'
        db.create_table('account_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Region'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.City'])),
            ('leaders', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=255, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('featuring', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('mood', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('account', ['Group'])

        # Adding M2M table for field styles on 'Group'
        db.create_table('account_group_styles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['account.group'], null=False)),
            ('style', models.ForeignKey(orm['account.style'], null=False))
        ))
        db.create_unique('account_group_styles', ['group_id', 'style_id'])

        # Adding model 'Membership'
        db.create_table('account_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('singer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Singer'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Group'])),
            ('date_joined', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('invite_reason', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
        ))
        db.send_create_signal('account', ['Membership'])

        # Adding model 'News'
        db.create_table('account_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('account', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'Direction'
        db.delete_table('account_direction')

        # Deleting model 'Style'
        db.delete_table('account_style')

        # Deleting model 'Country'
        db.delete_table('account_country')

        # Deleting model 'Region'
        db.delete_table('account_region')

        # Deleting model 'City'
        db.delete_table('account_city')

        # Deleting model 'Category'
        db.delete_table('account_category')

        # Deleting model 'CustomUser'
        db.delete_table('account_customuser')

        # Deleting model 'Singer'
        db.delete_table('account_singer')

        # Removing M2M table for field directions on 'Singer'
        db.delete_table('account_singer_directions')

        # Removing M2M table for field styles on 'Singer'
        db.delete_table('account_singer_styles')

        # Deleting model 'Group'
        db.delete_table('account_group')

        # Removing M2M table for field styles on 'Group'
        db.delete_table('account_group_styles')

        # Deleting model 'Membership'
        db.delete_table('account_membership')

        # Deleting model 'News'
        db.delete_table('account_news')


    models = {
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
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
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
        'account.news': {
            'Meta': {'object_name': 'News'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
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
        }
    }

    complete_apps = ['account']
