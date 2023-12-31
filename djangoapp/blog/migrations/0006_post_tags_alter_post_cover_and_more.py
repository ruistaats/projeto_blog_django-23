# Generated by Django 5.0 on 2023-12-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_created_by_post_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, default='', to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='posts/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_in_post_content',
            field=models.BooleanField(default=True, help_text='Se marcado, exibirá a capa dentro do post.'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcado para o post ser exibido publicamente.'),
        ),
    ]
