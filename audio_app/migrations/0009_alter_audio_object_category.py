# Generated by Django 4.1.2 on 2023-01-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_app', '0008_audio_object_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_object',
            name='category',
            field=models.CharField(choices=[('NS', 'Nature Sounds'), ('GM', 'Guided Meditations'), ('BE', 'Breathing Exercises'), ('S', 'Stories'), ('BB', 'Binaural Beats'), ('IR', 'Indian Ragas'), ('MM', 'Meditation Music'), ('SGM', 'Short Guided Meditation'), ('VC', 'Vocal Chanting')], default='MM', max_length=500),
        ),
    ]
