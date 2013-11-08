# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NodeArrowSpectrum'
        db.create_table(u'inventory_nodearrowspectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Arrow'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Node'])),
        ))
        db.send_create_signal(u'inventory', ['NodeArrowSpectrum'])

        # Adding unique constraint on 'NodeArrowSpectrum', fields ['node', 'relation']
        db.create_unique(u'inventory_nodearrowspectrum', ['node_id', 'relation_id'])

        # Adding model 'NodeLineSpectrum'
        db.create_table(u'inventory_nodelinespectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Line'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Node'])),
        ))
        db.send_create_signal(u'inventory', ['NodeLineSpectrum'])

        # Adding unique constraint on 'NodeLineSpectrum', fields ['node', 'relation']
        db.create_unique(u'inventory_nodelinespectrum', ['node_id', 'relation_id'])

        # Adding model 'NodeTriangleSpectrum'
        db.create_table(u'inventory_nodetrianglespectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_z', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Triangle'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Node'])),
        ))
        db.send_create_signal(u'inventory', ['NodeTriangleSpectrum'])

        # Adding unique constraint on 'NodeTriangleSpectrum', fields ['node', 'relation']
        db.create_unique(u'inventory_nodetrianglespectrum', ['node_id', 'relation_id'])

        # Adding model 'NodeCrossSpectrum'
        db.create_table(u'inventory_nodecrossspectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cross'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Node'])),
        ))
        db.send_create_signal(u'inventory', ['NodeCrossSpectrum'])

        # Adding unique constraint on 'NodeCrossSpectrum', fields ['node', 'relation']
        db.create_unique(u'inventory_nodecrossspectrum', ['node_id', 'relation_id'])

        # Adding model 'EdgeArrowSpectrum'
        db.create_table(u'inventory_edgearrowspectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Arrow'])),
            ('edge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Edge'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeArrowSpectrum'])

        # Adding unique constraint on 'EdgeArrowSpectrum', fields ['edge', 'relation']
        db.create_unique(u'inventory_edgearrowspectrum', ['edge_id', 'relation_id'])

        # Adding model 'EdgeLineSpectrum'
        db.create_table(u'inventory_edgelinespectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Line'])),
            ('edge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Edge'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeLineSpectrum'])

        # Adding unique constraint on 'EdgeLineSpectrum', fields ['edge', 'relation']
        db.create_unique(u'inventory_edgelinespectrum', ['edge_id', 'relation_id'])

        # Adding model 'EdgeTriangleSpectrum'
        db.create_table(u'inventory_edgetrianglespectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_z', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Triangle'])),
            ('edge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Edge'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeTriangleSpectrum'])

        # Adding unique constraint on 'EdgeTriangleSpectrum', fields ['edge', 'relation']
        db.create_unique(u'inventory_edgetrianglespectrum', ['edge_id', 'relation_id'])

        # Adding model 'EdgeCrossSpectrum'
        db.create_table(u'inventory_edgecrossspectrum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cross'])),
            ('edge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Edge'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeCrossSpectrum'])

        # Adding unique constraint on 'EdgeCrossSpectrum', fields ['edge', 'relation']
        db.create_unique(u'inventory_edgecrossspectrum', ['edge_id', 'relation_id'])

        # Adding model 'Node'
        db.create_table(u'inventory_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('node_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Node'])

        # Adding model 'Edge'
        db.create_table(u'inventory_edge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('source_node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_node', to=orm['inventory.Node'])),
            ('target_node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='target_node', to=orm['inventory.Node'])),
            ('transaction_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Edge'])


    def backwards(self, orm):
        # Removing unique constraint on 'EdgeCrossSpectrum', fields ['edge', 'relation']
        db.delete_unique(u'inventory_edgecrossspectrum', ['edge_id', 'relation_id'])

        # Removing unique constraint on 'EdgeTriangleSpectrum', fields ['edge', 'relation']
        db.delete_unique(u'inventory_edgetrianglespectrum', ['edge_id', 'relation_id'])

        # Removing unique constraint on 'EdgeLineSpectrum', fields ['edge', 'relation']
        db.delete_unique(u'inventory_edgelinespectrum', ['edge_id', 'relation_id'])

        # Removing unique constraint on 'EdgeArrowSpectrum', fields ['edge', 'relation']
        db.delete_unique(u'inventory_edgearrowspectrum', ['edge_id', 'relation_id'])

        # Removing unique constraint on 'NodeCrossSpectrum', fields ['node', 'relation']
        db.delete_unique(u'inventory_nodecrossspectrum', ['node_id', 'relation_id'])

        # Removing unique constraint on 'NodeTriangleSpectrum', fields ['node', 'relation']
        db.delete_unique(u'inventory_nodetrianglespectrum', ['node_id', 'relation_id'])

        # Removing unique constraint on 'NodeLineSpectrum', fields ['node', 'relation']
        db.delete_unique(u'inventory_nodelinespectrum', ['node_id', 'relation_id'])

        # Removing unique constraint on 'NodeArrowSpectrum', fields ['node', 'relation']
        db.delete_unique(u'inventory_nodearrowspectrum', ['node_id', 'relation_id'])

        # Deleting model 'NodeArrowSpectrum'
        db.delete_table(u'inventory_nodearrowspectrum')

        # Deleting model 'NodeLineSpectrum'
        db.delete_table(u'inventory_nodelinespectrum')

        # Deleting model 'NodeTriangleSpectrum'
        db.delete_table(u'inventory_nodetrianglespectrum')

        # Deleting model 'NodeCrossSpectrum'
        db.delete_table(u'inventory_nodecrossspectrum')

        # Deleting model 'EdgeArrowSpectrum'
        db.delete_table(u'inventory_edgearrowspectrum')

        # Deleting model 'EdgeLineSpectrum'
        db.delete_table(u'inventory_edgelinespectrum')

        # Deleting model 'EdgeTriangleSpectrum'
        db.delete_table(u'inventory_edgetrianglespectrum')

        # Deleting model 'EdgeCrossSpectrum'
        db.delete_table(u'inventory_edgecrossspectrum')

        # Deleting model 'Node'
        db.delete_table(u'inventory_node')

        # Deleting model 'Edge'
        db.delete_table(u'inventory_edge')


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
            'Meta': {'unique_together': "(('edge', 'relation'),)", 'object_name': 'EdgeArrowSpectrum'},
            'edge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Edge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Arrow']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.edgecrossspectrum': {
            'Meta': {'unique_together': "(('edge', 'relation'),)", 'object_name': 'EdgeCrossSpectrum'},
            'edge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Edge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Cross']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.edgelinespectrum': {
            'Meta': {'unique_together': "(('edge', 'relation'),)", 'object_name': 'EdgeLineSpectrum'},
            'edge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Edge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Line']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.edgetrianglespectrum': {
            'Meta': {'unique_together': "(('edge', 'relation'),)", 'object_name': 'EdgeTriangleSpectrum'},
            'edge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Edge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'Meta': {'unique_together': "(('node', 'relation'),)", 'object_name': 'NodeArrowSpectrum'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Node']"}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Arrow']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.nodecrossspectrum': {
            'Meta': {'unique_together': "(('node', 'relation'),)", 'object_name': 'NodeCrossSpectrum'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Node']"}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Cross']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.nodelinespectrum': {
            'Meta': {'unique_together': "(('node', 'relation'),)", 'object_name': 'NodeLineSpectrum'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Node']"}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Line']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        },
        u'inventory.nodetrianglespectrum': {
            'Meta': {'unique_together': "(('node', 'relation'),)", 'object_name': 'NodeTriangleSpectrum'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Node']"}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Triangle']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_z': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        }
    }

    complete_apps = ['inventory']