# Generated by Django 4.2.7 on 2024-01-19 18:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('is_active',), 'permissions': [('can_block_user', 'Может блокировать пользователя')],
                     'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
