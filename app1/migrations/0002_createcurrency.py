# Generated by Django 4.0 on 2022-06-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=225)),
                ('formal_name', models.CharField(max_length=225)),
                ('ISO_code', models.CharField(max_length=225)),
                ('show_in_millions', models.CharField(max_length=225)),
                ('suffix_to_amouny', models.CharField(max_length=225)),
                ('space_symbol_amount', models.CharField(max_length=225)),
                ('word_after_decimal', models.CharField(max_length=225)),
                ('decimal_no_in_words', models.CharField(max_length=225)),
            ],
        ),
    ]