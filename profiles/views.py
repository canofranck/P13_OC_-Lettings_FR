from django.shortcuts import render
from profiles.models import  Profile
from django.http import Http404


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    profiles_list = Profile.objects.all()
    if not profiles_list:
        raise Http404("No profiles found.")
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)
# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        raise Http404("Profile not found.")
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
