# Generated by Django 4.0.4 on 2022-07-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_remove_groupmodel_under_alter_groupmodel_alias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmodel',
            name='under',
            field=models.CharField(blank=True, default='Null', max_length=225),
        ),
    ]
