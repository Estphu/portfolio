from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def IndexView(request):
    return render(request, "core/home.html")


def load_more_content(request):
    # Content returned by HTMX
    return HttpResponse(
        "<p class='p-4 bg-green-100 rounded'>Here's some more content loaded dynamically with HTMX!\
        </p>"
    )


def show_avatar(request):
    return render(request, "core/components/avatar_modal.html")
