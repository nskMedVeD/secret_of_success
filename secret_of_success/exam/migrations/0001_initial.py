# Generated by Django 4.1.7 on 2023-03-10 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0006_alter_contestmaterial_other_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('institute', models.ForeignKey(default='Нет данных', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.institution', verbose_name='Учреждение')),
            ],
            options={
                'verbose_name': 'Эксперт',
                'verbose_name_plural': 'Эксперты',
            },
        ),
    ]
