# Generated by Django 5.1rc1 on 2024-07-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_food_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100, verbose_name='Тег')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='food.tagpost', verbose_name='Теги'),
        ),
    ]