# Generated by Django 3.1.7 on 2021-04-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartella',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cartella', models.CharField(help_text='inserire nome cartella', max_length=128)),
                ('tempo_riproduzione', models.IntegerField(help_text='secondi di riproduzione')),
            ],
            options={
                'verbose_name': 'Cartella',
                'verbose_name_plural': 'Cartelle',
            },
        ),
    ]
