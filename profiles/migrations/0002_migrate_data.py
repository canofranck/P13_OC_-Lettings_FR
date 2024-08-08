# profiles/migrations/0002_migrate_data.py
from django.db import migrations


def migrate_profile_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    for profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=profile.id,
            favorite_city=profile.favorite_city,
            user_id=profile.user_id
        )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profile_data),
    ]
