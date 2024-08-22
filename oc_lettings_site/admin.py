"""
This module registers the Letting, Address, and Profile models with the Django
admin site.

Models:
    - Letting: Represents a property available for letting, including details
      such as title and address.
    - Address: Represents the address details associated with a letting.
    - Profile: Represents user profiles, including user-specific information.

Admin Registration:
    - Letting: Registered to be managed via the Django admin interface.
    - Address: Registered to be managed via the Django admin interface.
    - Profile: Registered to be managed via the Django admin interface.
"""

from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
