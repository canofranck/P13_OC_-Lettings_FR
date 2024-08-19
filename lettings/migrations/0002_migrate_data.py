# lettings/migrations/0002_migrate_data.py
from django.db import migrations

def migrate_address_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')
    for address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=address.id,
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code
        )

def migrate_letting_data(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')
    for letting in OldLetting.objects.all():
        NewLetting.objects.create(
            id=letting.id,
            title=letting.title,
            address_id=letting.address_id
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),

    ]

    operations = [
        migrations.RunPython(migrate_address_data),
        migrations.RunPython(migrate_letting_data),
    ]
