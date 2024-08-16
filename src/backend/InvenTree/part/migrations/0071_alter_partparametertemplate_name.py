# Generated by Django 3.2.4 on 2021-08-07 11:40

from django.db import migrations, models
import part.models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0070_alter_part_variant_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partparametertemplate',
            name='name',
            field=models.CharField(help_text='Parameter Name', max_length=100, unique=True, validators=[part.models.validate_template_name], verbose_name='Name'),
        ),
    ]
