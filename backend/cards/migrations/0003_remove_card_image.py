# Generated by Django 4.0.4 on 2022-04-15 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_charisma_alter_card_intelligence_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='image',
        ),
    ]