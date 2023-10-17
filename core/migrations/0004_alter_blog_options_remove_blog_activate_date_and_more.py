# Generated by Django 4.2.6 on 2023-10-17 08:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_requests'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='activate_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='deactivate_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='status',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('0', 'featured'), ('1', 'normal')], default='ABCD', max_length=50),
        ),
        migrations.AddField(
            model_name='blog',
            name='project',
            field=models.CharField(choices=[('0', 'motors'), ('1', 'creatives')], default='ABCD', max_length=50),
        ),
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default='ABCD', verbose_name='Post Summary'),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='ABCD', upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Compose content'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Post Title'),
        ),
    ]