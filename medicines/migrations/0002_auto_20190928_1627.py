# Generated by Django 2.2.5 on 2019-09-28 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicines',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='medicines',
            old_name='Laboratory',
            new_name='laboratory',
        ),
    ]
