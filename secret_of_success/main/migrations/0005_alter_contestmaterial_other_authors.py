# Generated by Django 4.1.7 on 2023-03-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_author_options_alter_institution_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestmaterial',
            name='other_authors',
            field=models.ManyToManyField(null=True, related_name='other_author', to='main.author'),
        ),
    ]
