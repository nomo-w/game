# Generated by Django 2.2.4 on 2019-09-04 06:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test_pay', '0002_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(max_length=255, verbose_name='支付总类型')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('method_code', models.CharField(max_length=125, verbose_name='支付类型代码')),
                ('image_path', models.CharField(max_length=500, verbose_name='展示图片')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 9, 4, 6, 36, 51, 255973, tzinfo=utc), verbose_name='创建时间')),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 9, 4, 6, 36, 51, 255991, tzinfo=utc), verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255, verbose_name='厂商名')),
                ('vendor_url', models.URLField(max_length=500, verbose_name='厂商的支付url')),
                ('vendor_sign', models.CharField(max_length=500, verbose_name='厂商加密数据格式')),
                ('vendor_header', models.CharField(max_length=255, verbose_name='厂商所需请求头内容')),
                ('vendor_character', models.CharField(max_length=20, verbose_name='厂商所需字符编码')),
                ('vendor_sign_method', models.CharField(max_length=255, verbose_name='厂商使用的加密方法')),
                ('vendor_pubkey', models.CharField(max_length=500, verbose_name='厂商所需公钥路径')),
                ('vendor_prikey', models.CharField(max_length=500, verbose_name='厂商所需私钥路径')),
                ('vendor_params', models.CharField(max_length=500, verbose_name='子商户所需参数')),
                ('vendor_memcode', models.CharField(max_length=100, verbose_name='子商户号')),
                ('vendor_callback', models.URLField(verbose_name='提供给子商户的回调地址')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 9, 4, 6, 36, 51, 256355, tzinfo=utc), verbose_name='创建时间')),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 9, 4, 6, 36, 51, 256370, tzinfo=utc), verbose_name='更新时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(max_length=255, verbose_name='支付子类型')),
                ('vendor_paycode', models.CharField(max_length=255, verbose_name='厂商支付码')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('is_fast', models.CharField(max_length=10, verbose_name='是否好用快速')),
                ('image_path', models.CharField(max_length=500, verbose_name='展示图片')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 9, 4, 6, 36, 51, 256835, tzinfo=utc), verbose_name='创建时间')),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 9, 4, 6, 36, 51, 256850, tzinfo=utc), verbose_name='更新时间')),
                ('pay_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='pay.Payment_type', verbose_name='对应的支付总类型')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='pay.Payment_vendor', verbose_name='对应的厂商')),
            ],
        ),
    ]
