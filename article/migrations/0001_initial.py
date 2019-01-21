# Generated by Django 2.1.5 on 2019-01-15 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='文章标题')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('label', models.CharField(max_length=20, null=True, verbose_name='标签')),
                ('content', models.CharField(max_length=2048, verbose_name='文章内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]