# Generated by Django 2.1 on 2020-09-01 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetInvestment', '0002_auto_20200604_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAccount', models.CharField(max_length=20, unique=True)),
                ('userPasswd', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=40)),
                ('userPhone', models.CharField(max_length=20)),
                ('userAddress', models.CharField(max_length=100)),
                ('userImg', models.CharField(max_length=150)),
                ('userRank', models.IntegerField()),
                ('userToken', models.CharField(max_length=50)),
            ],
        ),
    ]
