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

        # Adding field 'Triangle.taxonomy'
        db.add_column(u'core_triangle', 'taxonomy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cross.taxonomy'
        db.add_column(u'core_cross', 'taxonomy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Arrow.taxonomy'
        db.add_column(u'core_arrow', 'taxonomy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Line.taxonomy'
        db.add_column(u'core_line', 'taxonomy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Taxonomy'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Taxonomy'
        db.delete_table(u'core_taxonomy')

        # Deleting field 'Triangle.taxonomy'
        db.delete_column(u'core_triangle', 'taxonomy_id')

        # Deleting field 'Cross.taxonomy'
        db.delete_column(u'core_cross', 'taxonomy_id')

        # Deleting field 'Arrow.taxonomy'
        db.delete_column(u'core_arrow', 'taxonomy_id')

        # Deleting field 'Line.taxonomy'
        db.delete_column(u'core_line', 'taxonomy_id')


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