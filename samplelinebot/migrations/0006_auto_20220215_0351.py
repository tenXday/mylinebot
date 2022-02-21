# Generated by Django 3.2.6 on 2022-02-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplelinebot', '0005_rename_type_name_script_type_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script_pnumber',
            old_name='intro',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='script_type',
            old_name='intro',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='script_list',
            name='photo',
            field=models.URLField(default=0, help_text='請輸入劇本示意圖', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='script_list',
            name='intro',
            field=models.CharField(help_text='請輸入介紹', max_length=500),
        ),
    ]
