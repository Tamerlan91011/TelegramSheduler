# Generated by Django 4.2.1 on 2023-05-08 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_remove_user_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
    ]
