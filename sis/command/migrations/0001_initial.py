# Generated by Django 5.0.4 on 2024-05-01 06:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.TextField(choices=[(1, 'Summer'), (2, 'Fall'), (3, 'Spring')])),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('credit_hours', models.IntegerField()),
                ('mandatory', models.BooleanField()),
                ('minimum_level', models.PositiveSmallIntegerField(default=1)),
                ('available', models.BooleanField(default=False)),
                ('prerequisites', models.ManyToManyField(to='command.course')),
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='command.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userinfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('degree', models.CharField(max_length=250)),
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='command.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.TextField(choices=[(1, 'Sun'), (2, 'Mon'), (3, 'Tue'), (4, 'Wed'), (5, 'Thu')])),
                ('timeslot', models.TextField(choices=[(1, '09:00 - 10:30'), (2, '10:45 - 12:15'), (3, '12:30 - 02:00'), (4, '02:15 - 03:45')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.course', to_field='code')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.room')),
            ],
        ),
    ]
