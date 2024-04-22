# Generated by Django 5.0.4 on 2024-04-22 20:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('command', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgpa', models.FloatField()),
                ('major', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='command.major')),
                ('userinfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classwork_marks', models.IntegerField()),
                ('homework_marks', models.IntegerField()),
                ('midterm_mark', models.IntegerField()),
                ('final_mark', models.IntegerField()),
                ('gpa', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.instructor')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]