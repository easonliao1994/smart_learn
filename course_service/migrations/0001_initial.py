# Generated by Django 4.1 on 2023-06-21 16:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='course_service/courses/')),
                ('description', models.TextField(blank=True, null=True)),
                ('difficulty', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20, null=True)),
                ('prerequisites', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('is_certified', models.BooleanField(default=False)),
                ('reviews', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('average_rating', models.FloatField(default=0)),
                ('price', models.FloatField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=30, null=True)),
                ('is_available', models.BooleanField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='user_service.instructorprofile')),
            ],
            options={
                'ordering': ['price'],
            },
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
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='module_service/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course_service.course')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagModule',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_service.module')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_service.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to='course_service.lesson')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
                'ordering': ('updated_at',),
            },
        ),
        migrations.AddField(
            model_name='module',
            name='tags',
            field=models.ManyToManyField(blank=True, through='course_service.TagModule', to='course_service.tag'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module', to='course_service.module'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_service.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['updated_at'],
                'unique_together': {('user', 'course')},
            },
        ),
        migrations.AddIndex(
            model_name='module',
            index=models.Index(fields=['id'], name='course_serv_id_5ef479_idx'),
        ),
        migrations.AddIndex(
            model_name='module',
            index=models.Index(fields=['created_at'], name='course_serv_created_94876f_idx'),
        ),
    ]
