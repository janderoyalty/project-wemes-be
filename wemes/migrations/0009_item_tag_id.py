# Generated by Django 4.0.6 on 2022-08-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wemes', '0008_remove_item_tag_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tag_id',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
    ]