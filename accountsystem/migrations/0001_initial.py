# Generated by Django 2.1.7 on 2019-04-26 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('account', models.CharField(choices=[('现金', '现金'), ('银行卡', '银行卡'), ('支付宝', '支付宝')], max_length=4)),
                ('outcometype', models.CharField(choices=[('服饰', '服饰'), ('食品酒水', '食品酒水'), ('居家物业', '居家物业'), ('行车交通', '行车交通'), ('文化教育', '文化教育'), ('休闲娱乐', '休闲娱乐')], max_length=4)),
                ('people', models.CharField(default='try', max_length=8)),
                ('money', models.FloatField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('username', models.ForeignKey(default='lyj', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('account', models.CharField(choices=[('现金', '现金'), ('银行卡', '银行卡'), ('支付宝', '支付宝')], max_length=4)),
                ('incometype', models.CharField(choices=[('工资', '工资'), ('奖金补贴', '奖金补贴'), ('投资分红', '投资分红'), ('其他', '其他')], max_length=4)),
                ('people', models.CharField(default='try', max_length=8)),
                ('money', models.FloatField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('username', models.ForeignKey(default='lyj', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(default='try', max_length=8, unique=True)),
                ('member_relation', models.CharField(choices=[('自己', '自己'), ('夫妻', '夫妻'), ('父子', '父子'), ('父女', '父女'), ('母子', '母子'), ('母女', '母女'), ('兄弟姐妹', '兄弟姐妹'), ('其他', '其他')], max_length=4)),
                ('member_password', models.CharField(default='111111', help_text='成员密码，默认为111111', max_length=20)),
                ('description', models.TextField(null=True)),
                ('username', models.ForeignKey(default='lyj', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
