# Generated by Django 4.0.4 on 2022-06-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_suffix_to_amouny_createcurrency_suffix_to_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcurrency',
            name='decimal_places',
            field=models.CharField(default=2, max_length=225),
        ),
    ]
