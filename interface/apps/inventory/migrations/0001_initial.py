# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NodeRelationMixin'
        db.create_table(u'inventory_noderelationmixin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Node'])),
        ))
        db.send_create_signal(u'inventory', ['NodeRelationMixin'])

        # Adding model 'NodeArrowSpectrum'
        db.create_table(u'inventory_nodearrowspectrum', (
            (u'noderelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.NodeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Arrow'])),
        ))
        db.send_create_signal(u'inventory', ['NodeArrowSpectrum'])

        # Adding model 'NodeLineSpectrum'
        db.create_table(u'inventory_nodelinespectrum', (
            (u'noderelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.NodeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Line'])),
        ))
        db.send_create_signal(u'inventory', ['NodeLineSpectrum'])

        # Adding model 'NodeTriangleSpectrum'
        db.create_table(u'inventory_nodetrianglespectrum', (
            (u'noderelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.NodeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_z', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Triangle'])),
        ))
        db.send_create_signal(u'inventory', ['NodeTriangleSpectrum'])

        # Adding model 'NodeCrossSpectrum'
        db.create_table(u'inventory_nodecrossspectrum', (
            (u'noderelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.NodeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cross'])),
        ))
        db.send_create_signal(u'inventory', ['NodeCrossSpectrum'])

        # Adding model 'EdgeRelationMixin'
        db.create_table(u'inventory_edgerelationmixin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Edge'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeRelationMixin'])

        # Adding model 'EdgeArrowSpectrum'
        db.create_table(u'inventory_edgearrowspectrum', (
            (u'edgerelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.EdgeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Arrow'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeArrowSpectrum'])

        # Adding model 'EdgeLineSpectrum'
        db.create_table(u'inventory_edgelinespectrum', (
            (u'edgerelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.EdgeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Line'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeLineSpectrum'])

        # Adding model 'EdgeTriangleSpectrum'
        db.create_table(u'inventory_edgetrianglespectrum', (
            (u'edgerelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.EdgeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_z', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Triangle'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeTriangleSpectrum'])

        # Adding model 'EdgeCrossSpectrum'
        db.create_table(u'inventory_edgecrossspectrum', (
            (u'edgerelationmixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.EdgeRelationMixin'], unique=True, primary_key=True)),
            ('value_x', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('value_y', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cross'])),
        ))
        db.send_create_signal(u'inventory', ['EdgeCrossSpectrum'])

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
        # Deleting model 'NodeRelationMixin'
        db.delete_table(u'inventory_noderelationmixin')

        # Deleting model 'NodeArrowSpectrum'
        db.delete_table(u'inventory_nodearrowspectrum')

        # Deleting model 'NodeLineSpectrum'
        db.delete_table(u'inventory_nodelinespectrum')

        # Deleting model 'NodeTriangleSpectrum'
        db.delete_table(u'inventory_nodetrianglespectrum')

        # Deleting model 'NodeCrossSpectrum'
        db.delete_table(u'inventory_nodecrossspectrum')

        # Deleting model 'EdgeRelationMixin'
        db.delete_table(u'inventory_edgerelationmixin')

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Node']"})
        },
        u'inventory.nodetrianglespectrum': {
            'Meta': {'object_name': 'NodeTriangleSpectrum', '_ormbases': [u'inventory.NodeRelationMixin']},
            u'noderelationmixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['inventory.NodeRelationMixin']", 'unique': 'True', 'primary_key': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Triangle']"}),
            'value_x': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_y': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'value_z': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'})
        }
    }

    complete_apps = ['inventory']