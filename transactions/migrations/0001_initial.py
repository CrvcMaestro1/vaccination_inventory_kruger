# Generated by Django 3.2.16 on 2022-10-17 17:45

from django.db import migrations, models
import django.db.models.deletion
import transactions.model_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('status', models.BooleanField(default=True)),
                ('identification', models.CharField(max_length=10, validators=[transactions.model_validators.validate_identification], verbose_name='Identification')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
        ),
        migrations.CreateModel(
            name='EmployeeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('home_address', models.CharField(max_length=250, verbose_name='Home Address')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('vaccination_status', models.CharField(blank=True, choices=[('vaccinated', 'VACCINATED'), ('non-vaccinated', 'NON-VACCINATED')], default='non-vaccinated', max_length=50, verbose_name='Vaccination Status')),
                ('vaccine_type', models.CharField(blank=True, choices=[('sputnik', 'SPUTNIK'), ('astrazeneca', 'ASTRAZENECA'), ('pfizer', 'PFIZER'), ('jhonson&jhonson', 'JHONSON&JHONSON')], max_length=50, verbose_name='Vaccine Type')),
                ('vaccination_date', models.DateField(blank=True, verbose_name='Vaccination Date')),
                ('doses_number', models.IntegerField(blank=True, verbose_name='Doses Number')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
