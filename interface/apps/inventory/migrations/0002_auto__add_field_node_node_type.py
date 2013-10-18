# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Node.node_type'
        db.add_column(u'inventory_node', 'node_type',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Node.node_type'
        db.delete_column(u'inventory_node', 'node_type')


    models = {
        u'inventory.edge': {
            'Meta': {'object_name': 'Edge'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'source_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_node'", 'to': u"orm['inventory.Node']"}),
            'target_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'target_node'", 'to': u"orm['inventory.Node']"}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'inventory.node': {
            'Meta': {'ordering': "['name']", 'object_name': 'Node'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inventory.Node']", 'through': u"orm['inventory.Edge']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'node_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['inventory']