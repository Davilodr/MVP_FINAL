# Generated by Django 4.1.3 on 2022-11-28 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
                ('dia_actual', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
