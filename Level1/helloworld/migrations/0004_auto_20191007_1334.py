# Generated by Django 2.2.6 on 2019-10-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0003_currentobjective'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64)),
                ('course_provider', models.CharField(max_length=64)),
                ('course_grade', models.CharField(max_length=16)),
                ('course_start', models.DateField()),
                ('course_end', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='previoustitle',
            name='job_desc',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]