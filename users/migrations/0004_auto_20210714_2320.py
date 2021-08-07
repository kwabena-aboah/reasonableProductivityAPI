# Generated by Django 3.1.1 on 2021-07-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210714_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fb_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]