# Generated by Django 4.1.2 on 2022-10-27 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0004_favorite_remove_category_cat_link_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='resource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='freeshelf.resource'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='Created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
