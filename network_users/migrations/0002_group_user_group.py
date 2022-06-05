# Generated by Django 4.0.5 on 2022-06-03 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('public', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='network_users.group'),
        ),
    ]