# Generated by Django 2.2.4 on 2019-09-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_game', '0003_auto_20190910_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamevendor',
            name='gameAlias',
            field=models.CharField(default=1, max_length=255, verbose_name='别名'),
            preserve_default=False,
        ),
    ]