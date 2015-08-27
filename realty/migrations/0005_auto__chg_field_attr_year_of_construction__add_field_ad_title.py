# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Attr.year_of_construction'
        db.alter_column(u'realty_attr', 'year_of_construction', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'Ad.title'
        db.add_column(u'realty_ad', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Attr.year_of_construction'
        db.alter_column(u'realty_attr', 'year_of_construction', self.gf('realty.custom_fields.YearField')())
        # Deleting field 'Ad.title'
        db.delete_column(u'realty_ad', 'title')


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
            'house': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen_space': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'living_space': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['realty.Object_type']"}),
            'rooms_amount': ('django.db.models.fields.IntegerField', [], {}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wc_type': ('django.db.models.fields.IntegerField', [], {}),
            'year_of_construction': ('django.db.models.fields.IntegerField', [], {})
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