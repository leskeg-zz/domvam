# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Object_type'
        db.create_table(u'realty_object_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'realty', ['Object_type'])

        # Adding model 'Attr'
        db.create_table(u'realty_attr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realty.Object_type'])),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('house', self.gf('django.db.models.fields.IntegerField')()),
            ('rooms_amount', self.gf('django.db.models.fields.IntegerField')()),
            ('living_space', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('year_of_construction', self.gf('realty.custom_fields.YearField')()),
            ('floors_amount', self.gf('django.db.models.fields.IntegerField')()),
            ('floor', self.gf('django.db.models.fields.IntegerField')()),
            ('kitchen_space', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('wc_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'realty', ['Attr'])

        # Adding model 'Ad'
        db.create_table(u'realty_ad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realty.Region'])),
        ))
        db.send_create_signal(u'realty', ['Ad'])


        # Changing field 'Region.name'
        db.alter_column(u'realty_region', 'name', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Deleting model 'Object_type'
        db.delete_table(u'realty_object_type')

        # Deleting model 'Attr'
        db.delete_table(u'realty_attr')

        # Deleting model 'Ad'
        db.delete_table(u'realty_ad')


        # Changing field 'Region.name'
        db.alter_column(u'realty_region', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'realty.ad': {
            'Meta': {'object_name': 'Ad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['realty.Region']"})
        },
        u'realty.attr': {
            'Meta': {'object_name': 'Attr'},
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
            'year_of_construction': ('realty.custom_fields.YearField', [], {})
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