# Generated by Django 2.1.7 on 2019-04-30 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountsystem', '0004_auto_20190429_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expend',
            name='people',
            field=models.ForeignKey(default='自己', on_delete=django.db.models.deletion.DO_NOTHING, to='accountsystem.Member', to_field='member_name'),
        ),
        migrations.AlterField(
            model_name='income',
            name='people',
            field=models.ForeignKey(default='自己', on_delete=django.db.models.deletion.DO_NOTHING, to='accountsystem.Member', to_field='member_name'),
        ),
    ]
