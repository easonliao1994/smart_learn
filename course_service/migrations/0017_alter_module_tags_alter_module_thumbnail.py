# Generated by Django 4.1 on 2023-04-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0016_module_tag_alter_skillcertification_certificate_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, through='course_service.TagModule', to='course_service.tag'),
        ),
        migrations.AlterField(
            model_name='module',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='module_service/'),
        ),
    ]
