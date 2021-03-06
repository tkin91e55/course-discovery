from django.db import migrations


def create_switch(apps, schema_editor):
    """Create the publisher_add_instructor_feature switch if it does not already exist."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.get_or_create(name='publisher_add_instructor_feature', defaults={'active': False})


def delete_switch(apps, schema_editor):
    """Delete the publisher_add_instructor_feature switch."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.filter(name='publisher_add_instructor_feature').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('publisher', '0029_auto_20170119_0934'),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_switch, delete_switch),
    ]
