# Generated by Django 4.0.3 on 2022-06-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_alter_todoitem_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
