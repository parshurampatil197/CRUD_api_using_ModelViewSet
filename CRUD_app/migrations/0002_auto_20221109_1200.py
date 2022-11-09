# Generated by Django 3.2.16 on 2022-11-09 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='CRUD_app.author'),
        ),
    ]
