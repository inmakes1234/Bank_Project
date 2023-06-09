# Generated by Django 4.1.7 on 2023-05-15 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dist_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=250)),
                ('Dist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.district')),
            ],
        ),
        migrations.CreateModel(
            name='Account_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('phn', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('account_type', models.CharField(choices=[('SA', 'Savings Account'), ('CU', 'Current Account'), ('FD', 'Fixed Deposit Account'), ('MM', 'Money Market Account'), ('CH', 'Cheque Account')], default='SA', max_length=2)),
                ('has_debit_card', models.BooleanField(default=False)),
                ('has_credit_card', models.BooleanField(default=False)),
                ('has_cheque_book', models.BooleanField(default=False)),
                ('has_adhaar_card', models.BooleanField(default=False)),
                ('has_pan_card', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bank_app.branches')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.district')),
            ],
        ),
    ]
