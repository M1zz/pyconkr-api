# Generated by Django 2.1.4 on 2019-01-16 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190116_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('program_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Program')),
                ('conference_field', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('api.program',),
        ),
    ]
