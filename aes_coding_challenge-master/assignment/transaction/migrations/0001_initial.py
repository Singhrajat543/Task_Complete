# Generated by Django 3.1.1 on 2021-09-28 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('short_name', models.CharField(max_length=50, unique=True)),
                ('blend_pct', models.CharField(max_length=50)),
                ('twists', models.PositiveIntegerField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='BranchMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('contact_person_name', models.CharField(max_length=20)),
                ('gst_number', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=10)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyLedgerMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('gst_number', models.CharField(max_length=20, unique=True)),
                ('supplier_status', models.BooleanField(default=False)),
                ('address1', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('remarks', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColorMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('short_name', models.CharField(max_length=20)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.articlemaster')),
            ],
        ),
    ]
