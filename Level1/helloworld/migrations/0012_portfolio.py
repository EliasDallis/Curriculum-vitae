# Generated by Django 2.2.5 on 2019-10-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0011_auto_20191016_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
            ],
        ),
    ]