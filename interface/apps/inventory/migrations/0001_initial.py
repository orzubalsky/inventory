# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'inventory_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
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
        # Deleting model 'Node'
        db.delete_table(u'inventory_node')

        # Deleting model 'Edge'
        db.delete_table(u'inventory_edge')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'Meta': {'object_name': 'Node'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'related_to': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related nodes'", 'symmetrical': 'False', 'through': u"orm['inventory.Edge']", 'to': u"orm['inventory.Node']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['inventory']