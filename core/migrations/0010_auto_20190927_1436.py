# Generated by Django 2.2.5 on 2019-09-27 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190925_1434'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='starhistory',
            unique_together={('repository', 'monthly_date')},
        ),
    ]
