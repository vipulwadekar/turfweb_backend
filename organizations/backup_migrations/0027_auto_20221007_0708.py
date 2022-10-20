# Generated by Django 3.2.15 on 2022-10-07 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0026_auto_20221007_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['image'],
            },
        ),
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='organizations.images'),
        ),
    ]