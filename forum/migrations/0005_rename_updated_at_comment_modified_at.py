# Generated by Django 3.2.5 on 2021-07-16 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='updated_at',
            new_name='modified_at',
        ),
    ]
