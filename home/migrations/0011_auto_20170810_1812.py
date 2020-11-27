# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 18:12
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170808_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('logo', wagtail.images.blocks.ImageChooserBlock()), ('date', wagtail.core.blocks.DateBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('quote', wagtail.core.blocks.RichTextBlock())]),
        ),
    ]
