# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Taxonomy'
        db.create_table(u'inventory_taxonomy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'inventory', ['Taxonomy'])

        # Adding field 'NodeRelationMixin.taxonomy'
        db.add_column(u'inventory_noderelationmixin', 'taxonomy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Taxonomy'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'EdgeRelationMixin.taxonomy'
        db.add_column(u'inventory_edgerelationmixin', 'taxonomy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Taxonomy'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Taxonomy'
        db.delete_table(u'inventory_taxonomy')

        # Deleting field 'NodeRelationMixin.taxonomy'
        db.delete_column(u'inventory_noderelationmixin', 'taxonomy_id')

        # Deleting field 'EdgeRelationMixin.taxonomy'
        db.delete_column(u'inventory_edgerelationmixin', 'taxonomy_id')


    models = {
        u'core.arrow': {
            'Meta': {'object_name': 'Arrow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.cross': {
            'Meta': {'object_name': 'Cross'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_x2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_y1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_y2': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_x2': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.triangle': {
            'Meta': {'object_name': 'Triangle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_x': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_y': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_z': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'inventory.edge': {
            'Meta': {'object_name': 'Edge'},
            'arrows': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Arrow']", 'through': u"orm['inventory.EdgeArrowSpectrum']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'crosses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Cross']", 'through': u"orm['inventory.EdgeCrossSpectrum']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Line']", 'through': u"orm['inventory.EdgeLineSpectrum']", 'symmetrical': 'False'}),
            'source_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_node'", 'to': u"orm['inventory.Node']"}),
            'target_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'target_node'", 'to': u"orm['inventory.Node']"}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'triangles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Triangle']", 'through': u"orm['inventory.EdgeTriangleSpectrum']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'inventory.edgearrowspectrum': {
            'Meta': {'object_name': 'EdgeArrowSpectrum', '_ormbases': [u'inventory.EdgeRelationMixin']},
            u'edgerelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.EdgeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Arrow']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.edgecrossspectrum': {
            'Meta': {'object_name': 'EdgeCrossSpectrum', '_ormbases': [u'inventory.EdgeRelationMixin']},
            u'edgerelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.EdgeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Cross']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.edgelinespectrum': {
            'Meta': {'object_name': 'EdgeLineSpectrum', '_ormbases': [u'inventory.EdgeRelationMixin']},
            u'edgerelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.EdgeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Line']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.edgerelationmixin': {
            'Meta': {'object_name': 'EdgeRelationMixin'},
            'edge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Edge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Taxonomy']", 'null': 'True', 'blank': 'True'})
        },
        u'inventory.edgetrianglespectrum': {
            'Meta': {'object_name': 'EdgeTriangleSpectrum', '_ormbases': [u'inventory.EdgeRelationMixin']},
            u'edgerelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.EdgeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Triangle']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_z': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.node': {
            'Meta': {'ordering': "['name']", 'object_name': 'Node'},
            'arrows': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Arrow']", 'through': u"orm['inventory.NodeArrowSpectrum']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'crosses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Cross']", 'through': u"orm['inventory.NodeCrossSpectrum']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inventory.Node']", 'through': u"orm['inventory.Edge']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Line']", 'through': u"orm['inventory.NodeLineSpectrum']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'node_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'triangles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Triangle']", 'through': u"orm['inventory.NodeTriangleSpectrum']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'inventory.nodearrowspectrum': {
            'Meta': {'object_name': 'NodeArrowSpectrum', '_ormbases': [u'inventory.NodeRelationMixin']},
            u'noderelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.NodeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Arrow']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.nodecrossspectrum': {
            'Meta': {'object_name': 'NodeCrossSpectrum', '_ormbases': [u'inventory.NodeRelationMixin']},
            u'noderelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.NodeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Cross']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.nodelinespectrum': {
            'Meta': {'object_name': 'NodeLineSpectrum', '_ormbases': [u'inventory.NodeRelationMixin']},
            u'noderelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.NodeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Line']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.noderelationmixin': {
            'Meta': {'object_name': 'NodeRelationMixin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Node']"}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Taxonomy']", 'null': 'True', 'blank': 'True'})
        },
        u'inventory.nodetrianglespectrum': {
            'Meta': {'object_name': 'NodeTriangleSpectrum', '_ormbases': [u'inventory.NodeRelationMixin']},
            u'noderelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.NodeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Triangle']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_z': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.taxonomy': {
            'Meta': {'object_name': 'Taxonomy'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['inventory']