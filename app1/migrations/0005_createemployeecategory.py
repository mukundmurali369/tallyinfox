# Generated by Django 4.0.4 on 2022-06-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_createcurrency_decimal_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEmployeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('allocate_revenue', models.CharField(max_length=225)),
                ('allocate_nonrevenue', models.CharField(max_length=225)),
            ],
        ),
    ]
