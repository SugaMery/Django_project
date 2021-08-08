# Generated by Django 3.0.5 on 2021-08-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(choices=[('Génie électromécanique', 'Génie électromécanique'), ('Génie civil', 'Génie civil'), ('Génie informatique et telecoms', 'Génie informatique et telecoms'), ('Tronc Commun', 'Tronc Commun')], max_length=300)),
                ('classe', models.CharField(choices=[('TC1', 'TC1'), ('TC2', 'TC2'), ('DIC1', 'DIC1'), ('DIC2', 'DIC2'), ('DIC3', 'DIC3')], max_length=200)),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('lieu', models.CharField(max_length=250)),
                ('pasword1', models.CharField(max_length=500)),
                ('pasword2', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
    ]
