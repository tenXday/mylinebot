# Generated by Django 3.2.6 on 2022-02-14 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samplelinebot', '0004_rename_theme_script_list_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script_type',
            old_name='type_name',
            new_name='type',
        ),
    ]
