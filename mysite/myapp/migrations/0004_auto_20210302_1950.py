# Generated by Django 3.1.7 on 2021-03-02 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bookuser_statusbool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='statusbool',
            name='status',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='myapp.Author'),
        ),
        migrations.DeleteModel(
            name='BookUser',
        ),
        migrations.DeleteModel(
            name='StatusBool',
        ),
        migrations.AddField(
            model_name='book',
            name='book_reserved',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.reader'),
        ),
    ]
