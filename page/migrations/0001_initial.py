# Generated by Django 3.1.7 on 2021-02-27 18:21

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
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('type', models.CharField(blank=True, choices=[('C', 'Cheap'), ('A', 'Average'), ('E', 'Expensive')], max_length=1, null=True)),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('reg_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
