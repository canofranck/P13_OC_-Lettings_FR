"""
oc_lettings_site/views.py

This module contains the Django view functions for rendering the home
page of the application.
"""

from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros,vitae dapibus nisi lorem
# dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis
# quis. Phasellus eleifend ex auctor venenatis tempus.Aliquam vitae erat ac
# orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim
# cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
        View function for displaying the home page.
        This view renders the 'index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page for the home page.
        """
    return render(request, "index.html")
