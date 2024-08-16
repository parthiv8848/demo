# Generated by Django 2.2.4 on 2019-08-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0013_auto_20190628_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Parameter Name', max_length=100)),
                ('data', models.CharField(help_text='Parameter Value', max_length=100)),
                ('part', models.ForeignKey(help_text='Parent Part', on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='part.Part')),
            ],
        ),
    ]
