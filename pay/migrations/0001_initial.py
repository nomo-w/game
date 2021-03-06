# Generated by Django 2.2.4 on 2019-08-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255, verbose_name='用户')),
                ('amount', models.CharField(max_length=255, verbose_name='付款金额')),
                ('orderno', models.CharField(max_length=255, verbose_name='订单号')),
                ('state', models.CharField(max_length=255, verbose_name='订单状态')),
                ('channel', models.CharField(max_length=255, verbose_name='支付方法')),
                ('ordertime', models.CharField(max_length=255, verbose_name='下单时间')),
            ],
        ),
    ]
