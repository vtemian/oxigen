# Generated by Django 3.0.11 on 2020-11-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0007_donor_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of Donor'),
        ),
    ]
