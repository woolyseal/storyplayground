# Generated by Django 4.2.16 on 2024-10-04 10:36

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rpgs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleplay',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Description'),
        ),
    ]
