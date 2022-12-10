from django.shortcuts import render

# Create your views here.
def index(request):
    name = request.GET.get("board", '반려동물동반식당')
    information_name = "모든게시판"
    information_list = ["반려동물동반식당", "반려동물동반카페", "동물병원"]

    context = {
        "name": name,
        "information_name": information_name,
        "information_list": information_list,
    }
    return render(request, "information/index.html",context)
    


def friends(request):
    return render(request, "information/friends.html")
