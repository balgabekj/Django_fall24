# Generated by Django 5.1.1 on 2024-10-04 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_id_alter_post_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='post',
            name='blog_post_created_45f0c6_idx',
        ),
    ]
