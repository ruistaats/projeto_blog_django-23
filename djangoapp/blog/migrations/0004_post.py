# Generated by Django 5.0 on 2023-12-20 00:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('excerpt', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisará estar marcado para a página ser exibida publicamente.')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='posts/%Y/%m')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='Exibe a imagem da capa também no conteúdo do Post?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
