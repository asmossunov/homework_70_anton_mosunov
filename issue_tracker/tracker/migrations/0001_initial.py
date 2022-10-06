# Generated by Django 3.2 on 2022-10-06 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст задачи')),
                ('description', models.TextField(blank=True, max_length=3000, verbose_name='Описание задачи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to='tracker.status', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to='tracker.type', verbose_name='Тип')),
            ],
        ),
    ]
