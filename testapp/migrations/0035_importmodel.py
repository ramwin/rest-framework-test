# Generated by Django 3.0.5 on 2020-04-16 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0034_database2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '测试导入导出',
                'verbose_name_plural': '测试导入导出',
            },
        ),
    ]
