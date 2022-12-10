from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "information/index.html")


def friends(request):

    return render(request, "information/friends.html")
