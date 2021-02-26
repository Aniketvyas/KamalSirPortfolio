# Generated by Django 3.0.5 on 2021-02-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsAndUpdates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=400)),
                ('image', models.FileField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
    ]
