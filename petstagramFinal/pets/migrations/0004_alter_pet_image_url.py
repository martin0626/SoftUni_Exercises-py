# Generated by Django 4.0.1 on 2022-01-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_alter_pet_type_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
