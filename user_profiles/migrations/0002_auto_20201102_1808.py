# Generated by Django 3.1.2 on 2020-11-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active_pack',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='active_pack_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
