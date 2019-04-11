# Generated by Django 2.1.3 on 2019-04-11 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djfauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTurnOver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_type', models.CharField(choices=[('out', '支出'), ('in', '收入'), ('exp', '消费')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('comment', models.CharField(max_length=500)),
                ('create_dt', models.DateField(verbose_name='created date')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='updated date')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('as_iden', models.CharField(max_length=200)),
                ('as_organ', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('bill_date', models.CharField(blank=True, max_length=200, null=True)),
                ('repayment_date', models.CharField(blank=True, max_length=200, null=True)),
                ('credit_limit', models.CharField(blank=True, max_length=200, null=True)),
                ('year_rate', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('create_dt', models.DateField(verbose_name='created date')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='updated date')),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetname', models.CharField(max_length=200)),
                ('detailtype', models.CharField(max_length=200)),
                ('create_dt', models.DateField(verbose_name='created date')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='updated date')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='as_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.AssetType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djfauth.User'),
        ),
        migrations.AddField(
            model_name='accountturnover',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Asset'),
        ),
        migrations.AddField(
            model_name='accountturnover',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djfauth.User'),
        ),
    ]