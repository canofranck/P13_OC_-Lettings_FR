import os
import sys


def main():
    """
    Sets the DJANGO_SETTINGS_MODULE environment variable
    to 'oc_lettings_site.settings'.
    Attempts to import and execute Django's command-line utility for
    administrative tasks.
    
    Raises:
        ImportError: If Django is not installed or not available on the
        PYTHONPATH environment variable, or if the virtual environment
        is not activated.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
