from django.shortcuts import render
from lettings.models import Letting

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum,
# nulla eget feugiat sagittis, sem mi convallis eros, vitae dapibus nisi
# lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque
# iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque
# cursus id.


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)

# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
# porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus
# urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean finibus
# faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim
# mattis enim, ac condimentum velit libero in magna. Suspendisse potenti. In
# tempus a nisi sed laoreet.Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# vamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer
# vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.


def letting(request, letting_id):
    try:
        letting = Letting.objects.get(id=int(letting_id))
    except Letting.DoesNotExist:
        error = f"Letting id n°{letting_id} does not exist !"
        return render(request, "404.html", {"error": error})
    except ValueError:
        error = f"ValueError : an number is requires but got : {letting_id}"
        return render(request, "404.html", {"error": error})
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
