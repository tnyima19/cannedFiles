# Generated by Django 4.2.4 on 2023-08-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0011_message_flash10_message_flash9_message_line10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='line1',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line10',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line2',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line3',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line4',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line5',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line6',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line7',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line8',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='line9',
            field=models.TextField(blank=True, max_length=17, null=True),
        ),
    ]
