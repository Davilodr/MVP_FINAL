# Generated by Django 4.1.2 on 2022-11-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PControl', '0003_supervisor_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalcc',
            name='direccion',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalcc',
            name='telefono',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldxtv',
            name='direccion',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldxtv',
            name='telefono',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
