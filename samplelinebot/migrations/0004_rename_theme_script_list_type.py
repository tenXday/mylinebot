# Generated by Django 3.2.6 on 2022-02-14 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samplelinebot', '0003_auto_20220215_0225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script_list',
            old_name='theme',
            new_name='type',
        ),
    ]
