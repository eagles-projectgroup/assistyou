# Generated by Django 5.0.7 on 2024-07-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='note', to='notes.tag'),
        ),
    ]
