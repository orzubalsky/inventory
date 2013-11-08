# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Taxonomy'
        db.create_table(u'core_taxonomy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Taxonomy'])

        # Adding model 'Arrow'
        db.create_table(u'core_arrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_x', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('taxonomy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Arrow'])

        # Adding model 'Line'
        db.create_table(u'core_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_x1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_x2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('taxonomy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Line'])

        # Adding model 'Triangle'
        db.create_table(u'core_triangle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_x', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_y', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_z', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('taxonomy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Triangle'])

        # Adding model 'Cross'
        db.create_table(u'core_cross', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_x1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_x2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_y1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_y2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('taxonomy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Cross'])


    def backwards(self, orm):
        # Deleting model 'Taxonomy'
        db.delete_table(u'core_taxonomy')

        # Deleting model 'Arrow'
        db.delete_table(u'core_arrow')

        # Deleting model 'Line'
        db.delete_table(u'core_line')

        # Deleting model 'Triangle'
        db.delete_table(u'core_triangle')

        # Deleting model 'Cross'
        db.delete_table(u'core_cross')


    models = {
        u'core.arrow': {
            'Meta': {'object_name': 'Arrow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Taxonomy']", 'null': 'True', 'blank': 'True'})
        },
        u'core.cross': {
            'Meta': {'object_name': 'Cross'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_x2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_y1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_y2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Taxonomy']", 'null': 'True', 'blank': 'True'})
        },
        u'core.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_x2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Taxonomy']", 'null': 'True', 'blank': 'True'})
        },
        u'core.taxonomy': {
            'Meta': {'object_name': 'Taxonomy'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'core.triangle': {
            'Meta': {'object_name': 'Triangle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_y': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_z': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Taxonomy']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']