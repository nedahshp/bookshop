# Generated by Django 4.0.5 on 2022-07-22 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_coment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.books'),
        ),
    ]