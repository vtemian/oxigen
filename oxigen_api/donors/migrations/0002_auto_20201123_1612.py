# Generated by Django 3.0.11 on 2020-11-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('target', models.FloatField(default=0)),
                ('amount_collected', models.FloatField(default=0)),
                ('donations', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name of Donor')),
                ('display_name', models.CharField(blank=True, max_length=255, verbose_name='Name of Donor')),
                ('amount', models.IntegerField()),
                ('comment', models.TextField(null=True)),
                ('is_company', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('supplier', models.CharField(max_length=255, null=True)),
                ('document', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('amount', models.FloatField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]