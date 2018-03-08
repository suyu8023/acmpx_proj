# Generated by Django 2.0.1 on 2018-03-08 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='证书编号')),
                ('student_no', models.CharField(max_length=32, verbose_name='学号')),
                ('student_class', models.CharField(max_length=32, verbose_name='班级')),
                ('student_name', models.CharField(max_length=32, verbose_name='姓名')),
                ('score', models.IntegerField(default=0, verbose_name='分数')),
                ('rank', models.IntegerField(default=0, verbose_name='排名')),
                ('idx', models.IntegerField(default=0, verbose_name='排序索引')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='培训名称')),
                ('title_en', models.CharField(max_length=128, verbose_name='培训名称（英文）')),
                ('started_at', models.DateField(verbose_name='培训开始日期')),
                ('ended_at', models.DateField(verbose_name='培训结束日期')),
                ('number_of_participants', models.IntegerField(default=0)),
                ('hidden', models.BooleanField(default=False, verbose_name='隐藏')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.AddField(
            model_name='certificate',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acmpx.Training'),
        ),
    ]
