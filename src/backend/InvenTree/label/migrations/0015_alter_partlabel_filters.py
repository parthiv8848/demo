# Generated by Django 4.2.14 on 2024-08-16 07:34

from django.db import migrations, models
import label.models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0014_alter_partlabel_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partlabel',
            name='filters',
            field=models.CharField(blank=True, help_text='Query filters', max_length=250, validators=[label.models.validate_part_filters], verbose_name='Filters'),
        ),
    ]
