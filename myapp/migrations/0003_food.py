# Generated by Django 2.2.1 on 2019-10-23 19:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_auto_20191023_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=25)),
                ('food_type', models.CharField(max_length=25)),
                ('food_rate', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete='CASCADE', related_name='foods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
