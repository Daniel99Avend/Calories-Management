# Generated by Django 2.2.3 on 2020-10-05 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20201005_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='food',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Blog.food'),
        ),
    ]