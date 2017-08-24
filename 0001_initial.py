from __future__ import unicode_literals

import agent.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

   initial = True

   dependencies = [
    ]

   operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20, validators=[agent.validators.validate_city])),
                ('state', models.CharField(max_length=20, validators=[agent.validators.validate_state])),
                ('landmark', models.CharField(max_length=50, validators=[agent.validators.validate_landmark])),
                ('pincode', models.CharField(max_length=10, validators=[agent.validators.validate_pincode])),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=15, validators=[agent.validators.validate_mobile_no])),
                ('phone_no', models.CharField(max_length=15, validators=[agent.validators.validate_phone_no])),
                ('email_id', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='agent.ContactInfo')),
                ('cuid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15, validators=[agent.validators.validate_first_name])),
                ('last_name', models.CharField(max_length=15, validators=[agent.validators.validate_last_name])),
                ('age', models.CharField(max_length=2, validators=[agent.validators.validate_age])),
                ('Addresses', models.ManyToManyField(to='agent.Address')),
            ],
            bases=('agent.contactinfo',),
        ),
    ]