# Generated by Django 3.0.7 on 2021-01-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201230_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimage',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]