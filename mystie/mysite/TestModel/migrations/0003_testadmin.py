# Generated by Django 2.2.7 on 2019-11-17 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20191112_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAdmin',
            fields=[
                ('test_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TestModel.Test')),
            ],
            bases=('TestModel.test',),
        ),
    ]