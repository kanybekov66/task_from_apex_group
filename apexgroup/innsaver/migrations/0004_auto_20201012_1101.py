# Generated by Django 3.1.2 on 2020-10-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innsaver', '0003_auto_20201012_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='firstName',
            field=models.CharField(default='', max_length=36),
        ),
        migrations.AlterField(
            model_name='human',
            name='patronymic',
            field=models.CharField(default='', max_length=36),
        ),
        migrations.AlterField(
            model_name='human',
            name='surname',
            field=models.CharField(default='', max_length=36),
        ),
    ]
