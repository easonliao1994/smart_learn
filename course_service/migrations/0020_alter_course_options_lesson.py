# Generated by Django 4.1 on 2023-04-21 15:01

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0019_alter_skillcertification_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['price']},
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_url', models.URLField(blank=True, null=True)),
                ('audio_url', models.URLField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('resources', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module', to='course_service.module')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
