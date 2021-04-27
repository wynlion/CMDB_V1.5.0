# Generated by Django 3.0.6 on 2021-04-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0029_attachment_devicelist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': '规范总览', 'verbose_name_plural': '规范总览'},
        ),
        migrations.AlterModelOptions(
            name='devicelist',
            options={'verbose_name': '设备管理', 'verbose_name_plural': '设备管理'},
        ),
        migrations.AddField(
            model_name='devicelist',
            name='accuracy',
            field=models.CharField(default='', max_length=64, verbose_name='量程/准确的(精度)'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='device_name',
            field=models.CharField(default='', max_length=64, verbose_name='仪器设备名称'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='device_number',
            field=models.CharField(default='', max_length=64, unique=True, verbose_name='仪器设备编号'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='device_type',
            field=models.CharField(choices=[('GJLSB', '钢筋类设备'), ('HXLSB', '化学类设备'), ('JLLSB', '集料类设备'), ('JALSB', '交安类设备'), ('LQHHLSB', '沥青混合料设备'), ('LQLSB', '沥青类设备'), ('QLLSB', '桥梁类设备'), ('SNHNTLSB', '水泥混凝土类设备'), ('SNLSB', '水泥类设备'), ('SNWJJLSB', '水泥外加剂类设备'), ('TGLSB', '土工类设备'), ('WJJHLSB', '无机结合料设备'), ('XCJCLSB', '现场检测类设备'), ('YSLSB', '岩石类设备'), ('ZHLSB', '综合类设备')], default='', max_length=64, verbose_name='仪器设备类别'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='next_type',
            field=models.CharField(choices=[('CK', '出库'), ('RK', '入库'), ('SJ', '送检'), ('DJ', '待检')], default='', max_length=64, verbose_name='设备下一步状态'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='out_sn',
            field=models.CharField(default='', max_length=64, unique=True, verbose_name='出厂编号'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='purchase_date',
            field=models.DateField(blank=True, null=True, verbose_name='购置日期'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='situation_type',
            field=models.CharField(choices=[('LH', '良好'), ('TY', '停用')], default='', max_length=64, verbose_name='仪器设备状态'),
        ),
        migrations.AddField(
            model_name='devicelist',
            name='size',
            field=models.CharField(default='', max_length=64, verbose_name='型号规格'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(max_length=128, verbose_name='规范标准名称'),
        ),
    ]
