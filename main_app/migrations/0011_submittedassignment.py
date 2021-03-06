# Generated by Django 3.0.5 on 2021-04-14 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_assignments_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='submittedAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submittedFile', models.FileField(upload_to='')),
                ('submited_onDate', models.DateField()),
                ('submited_onTime', models.TimeField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.assignments')),
                ('submitedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student')),
            ],
        ),
    ]
