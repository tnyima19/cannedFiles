# Generated by Django 4.2.4 on 2023-08-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0010_alter_message_scroll1_alter_message_scroll2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='flash10',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='flash9',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='line10',
            field=models.TextField(max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='line9',
            field=models.TextField(max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='scroll10',
            field=models.CharField(default='None', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='scroll9',
            field=models.CharField(default='None', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='transition_time10',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='message',
            name='transition_time9',
            field=models.IntegerField(default=2),
        ),
    ]
