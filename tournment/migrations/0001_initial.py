# Generated by Django 2.2.4 on 2020-04-21 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(help_text='upload image size less than 2.0MB', null=True, upload_to='profiles', verbose_name='PGN')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('last', models.CharField(max_length=125)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('Not Known', 'Not Known')], default='male', max_length=8, verbose_name='Gender')),
                ('rating', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='FIDE Rating')),
                ('title', models.CharField(choices=[('GM', 'GM'), ('MASTER', 'MASTER'), ('ROOKIE', 'ROOKIE'), ('WM', 'WM')], default='GM', max_length=8, verbose_name='Gender')),
                ('ranking', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='FIDE Ranking')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Players',
                'ordering': ['name', 'created'],
                'verbose_name': 'Player',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Tournment Name')),
                ('desc', models.CharField(max_length=250, null=True, verbose_name='Tournment Description')),
                ('location', models.CharField(max_length=50, null=True, verbose_name='Location')),
                ('country', models.CharField(max_length=50, null=True, verbose_name='Country')),
                ('laws', models.CharField(max_length=50, null=True, verbose_name='Laws Of Chess')),
                ('type', models.CharField(choices=[('Standard Chess Position', 'Standard Chess Position'), ('Chess960', 'Chess960'), ('King Of The Hill', 'King Of The Hill')], default='Standard Chess Position', max_length=25, null=True)),
                ('startdate', models.DateField(null=True, verbose_name='Start Date')),
                ('starttime', models.TimeField(blank=True, help_text='Tournment start time is on ..', null=True, verbose_name='Start Time')),
                ('enddate', models.DateField(null=True, verbose_name='End Date')),
                ('endtime', models.TimeField(blank=True, help_text='Tournment end time is on ..', null=True, verbose_name='End Time')),
                ('rounds', models.PositiveIntegerField(default=0, null=True, verbose_name='Number of Rounds')),
                ('status', models.CharField(default='pending', max_length=12)),
                ('is_approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tournments',
                'ordering': ['-created'],
                'verbose_name': 'Tournment',
            },
        ),
        migrations.CreateModel(
            name='Heats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds', models.PositiveIntegerField(default=0, null=True, verbose_name='Select Players per Rounds')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('player1', models.ForeignKey(max_length=125, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='tournment.Players')),
                ('player2', models.ForeignKey(max_length=125, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='tournment.Players')),
                ('tournment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tournment.Leave')),
            ],
            options={
                'verbose_name_plural': 'Heats',
                'ordering': ['tournment', 'created'],
                'verbose_name': 'Heat',
            },
        ),
    ]
