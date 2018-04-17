# Generated by Django 2.0 on 2018-04-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_events', '0035_change_event_kinds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='kind',
            field=models.CharField(choices=[('cinema', 'Cinema'), ('concert', 'Concert'), ('comedy', 'Comedy'), ('dance', 'Dance'), ('exhibition', 'Exhibition'), ('museum', 'Gallery/Museum'), ('gig', 'Gig'), ('theatre', 'Theatre'), ('misc', 'Other')], help_text='Used to categorise event. But any kind of Work can be added to any kind of Event.', max_length=20),
        ),
    ]