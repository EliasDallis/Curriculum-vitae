# Generated by Django 2.2.6 on 2019-10-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_previoustitle_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_obj_text', models.TextField()),
            ],
        ),
    ]
