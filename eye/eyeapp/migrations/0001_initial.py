# Generated by Django 4.0.3 on 2022-04-05 15:25

from django.db import migrations, models
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('session_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=70)),
                ('name', models.CharField(max_length=70)),
                ('data', jsonfield.fields.JSONField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=30)),
                ('sessions', models.ManyToManyField(to='eyeapp.event')),
            ],
        ),
    ]