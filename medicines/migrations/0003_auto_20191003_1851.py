# Generated by Django 2.2.5 on 2019-10-03 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_auto_20190928_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicines',
            options={'ordering': ['-created_at'], 'verbose_name': 'Medicine', 'verbose_name_plural': 'Medicines'},
        ),
        migrations.RenameField(
            model_name='medicines',
            old_name='date_created',
            new_name='created_at',
        ),
    ]
