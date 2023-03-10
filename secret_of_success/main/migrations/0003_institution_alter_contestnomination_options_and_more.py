# Generated by Django 4.1.7 on 2023-03-10 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contestnomination_alter_contestmaterial_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(default='000000', max_length=6, verbose_name='Индекс')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес учреждения')),
                ('name', models.CharField(max_length=255, verbose_name='Название учреждения')),
            ],
        ),
        migrations.AlterModelOptions(
            name='contestnomination',
            options={'ordering': ['nomination_letter'], 'verbose_name': 'Конкурсная номинация', 'verbose_name_plural': 'Конкурсные номинации'},
        ),
        migrations.AlterField(
            model_name='contestmaterial',
            name='nomination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.contestnomination', verbose_name='Номинация'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('institute', models.ForeignKey(default='Нет данных', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.institution', verbose_name='Учреждение')),
            ],
        ),
        migrations.AddField(
            model_name='contestmaterial',
            name='main_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.author', verbose_name='Руководитель авторской группы'),
        ),
        migrations.AddField(
            model_name='contestmaterial',
            name='other_authors',
            field=models.ManyToManyField(related_name='other_author', to='main.author'),
        ),
    ]
