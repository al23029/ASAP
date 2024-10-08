# Generated by Django 5.0.7 on 2024-08-09 06:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbridge', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('japanese', models.TextField(blank=True, null=True)),
                ('vietnamese', models.TextField(blank=True, null=True)),
                ('english', models.TextField(blank=True, null=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255)),
                ('latest_message_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_message_in_group', to='techbridge.groupmessage')),
            ],
        ),
        migrations.CreateModel(
            name='GroupThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_message_in_thread', to='techbridge.groupmessage')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbridge.group')),
            ],
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbridge.groupthread'),
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbridge.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('group', 'user')},
            },
        ),
    ]
