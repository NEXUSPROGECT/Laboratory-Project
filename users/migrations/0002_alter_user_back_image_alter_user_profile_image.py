# Generated by Django 5.1.1 on 2024-10-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='back_image',
            field=models.ImageField(blank=True, default='static/users_profile_images/defaultIconBack.png', null=True, upload_to='static/users_background_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/users_profile_images/defaultIconProfile.png', null=True, upload_to='static/users_profile_images'),
        ),
    ]
