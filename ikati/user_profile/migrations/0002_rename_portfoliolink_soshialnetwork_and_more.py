# Generated by Django 4.1.4 on 2022-12-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PortfolioLink',
            new_name='SoshialNetwork',
        ),
        migrations.AlterModelOptions(
            name='soshialnetwork',
            options={'verbose_name': 'soshial network', 'verbose_name_plural': 'soshial networks'},
        ),
        migrations.AddField(
            model_name='profile',
            name='Soshial_network',
            field=models.ManyToManyField(to='user_profile.soshialnetwork'),
        ),
    ]