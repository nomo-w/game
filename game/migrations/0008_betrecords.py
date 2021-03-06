# Generated by Django 2.2.4 on 2019-09-16 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_game', '0007_auto_20190912_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longmen_data', models.TextField(blank=True, null=True, verbose_name='龙门数据')),
                ('verdor_data', models.TextField(blank=True, null=True, verbose_name='厂商数据')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet', to='game.User', verbose_name='用户')),
            ],
        ),
    ]
