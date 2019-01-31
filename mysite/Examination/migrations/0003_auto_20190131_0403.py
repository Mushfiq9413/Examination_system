# Generated by Django 2.1.5 on 2019-01-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examination', '0002_auto_20190131_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='questions_exam',
            name='answer1',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='questions_exam',
            name='answer2',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='questions_exam',
            name='answer3',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='questions_exam',
            name='answer4',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='questions_exam',
            name='question_text',
            field=models.CharField(default='', max_length=300),
        ),
    ]
