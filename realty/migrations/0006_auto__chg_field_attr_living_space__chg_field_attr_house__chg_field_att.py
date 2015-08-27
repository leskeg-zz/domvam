# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Attr.living_space'
        db.alter_column(u'realty_attr', 'living_space', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

        # Changing field 'Attr.house'
        db.alter_column(u'realty_attr', 'house', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Attr.year_of_construction'
        db.alter_column(u'realty_attr', 'year_of_construction', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Attr.kitchen_space'
        db.alter_column(u'realty_attr', 'kitchen_space', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Attr.living_space'
        raise RuntimeError("Cannot reverse this migration. 'Attr.living_space' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Attr.living_space'
        db.alter_column(u'realty_attr', 'living_space', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # User chose to not deal with backwards NULL issues for 'Attr.house'
        raise RuntimeError("Cannot reverse this migration. 'Attr.house' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Attr.house'
        db.alter_column(u'realty_attr', 'house', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Attr.year_of_construction'
        raise RuntimeError("Cannot reverse this migration. 'Attr.year_of_construction' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Attr.year_of_construction'
        db.alter_column(u'realty_attr', 'year_of_construction', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Attr.kitchen_space'
        raise RuntimeError("Cannot reverse this migration. 'Attr.kitchen_space' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Attr.kitchen_space'
        db.alter_column(u'realty_attr', 'kitchen_space', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

    models = {
        u'realty.ad': {
            'Meta': {'object_name': 'Ad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['realty.Region']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'realty.attr': {
            'Meta': {'object_name': 'Attr'},
            'ad_obj': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['realty.Ad']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'floor': ('django.db.models.fields.IntegerField', [], {}),
            'floors_amount': ('django.db.models.fields.IntegerField', [], {}),
            'house': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen_space': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'living_space': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['realty.Object_type']"}),
            'rooms_amount': ('django.db.models.fields.IntegerField', [], {}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wc_type': ('django.db.models.fields.IntegerField', [], {}),
            'year_of_construction': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'realty.object_type': {
            'Meta': {'object_name': 'Object_type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'realty.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['realty']