# Generated by Django 3.1.1 on 2021-07-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profiles/')),
                ('fb_profile', models.URLField()),
                ('twitter_profile', models.URLField()),
                ('linkedin_profile', models.URLField()),
                ('website', models.URLField()),
            ],
        ),
    ]