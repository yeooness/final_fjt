from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from datetime import date
import json

from .models import Calendar

# 최초 인덱스 페이지 (로그인이 된 경우에는 Schedule 페이지로 이동하고, 로그인이 되어 있지 않는 경우 로그인 페이지로 이동함)
def index(request):
    today = date.today()
    # 오늘 날짜를 구함
    context = {"today_ymd": today.strftime("%Y-%m-%d")}
    if request.user.id != None:
        # index.html 페이지를 렌더링하도록 요청함
        return render(request, "schedule/index.html", context)
    else:
        # 로그인이 되어 있지 않기 때문에 로그인 페이지로 이동시킴
        return redirect("accounts:login")


# 현재 로그인된 사용자의 최근 등록된 이벤트 정보를 요청함
def get_events(request):
    if request.user.id != None:
        # 현재 로그인된 사용자의 화면에서 요청한 시작일자(start), 종료일자(end)에 대한 이벤트 정보를 읽어서 반환한다.
        data = list(
            Calendar.objects.filter(
                userId=request.user.id,
                start__gte=request.GET["start"][0:10],
                end__lte=request.GET["end"][0:10],
            ).values()
        )
        # 가져온 Calendar 데이터를 JSON 포맷으로 화면에 전달함
        return JsonResponse(data, safe=False)
    else:
        # 로그인이 되어 있지 않기 때문에 로그인 페이지로 이동시킴
        return redirect("accounts:login")


# 새로운 이벤트 정보를 등록함
def set_all_day_event(request):
    if request.user.id != None:
        # 화면에서 전달한 새로운 이벤트 JSON 데이터를 로딩함
        data = json.loads(request.body.decode("utf-8"))
        # Calendar Model에 화면에서 전달한 이벤트 정보를 세팅함
        calendar = Calendar(
            userId=request.user.id,
            title=data["title"],
            start=data["start"],
            end=data["end"],
            allDay=data["allDay"],
        )
        # Calendar 데이터를 전달함
        calendar.save()
        # 이벤트 저장한 후에 생성된 Calendar PK 아이디를 eventId 속성에 저장해서 JSON 포맷으로 반환함
        return JsonResponse({"result": "success", "eventId": calendar.id}, safe=False)
    else:
        # 로그인이 되어 있지 않기 때문에 로그인 페이지로 이동시킴
        return redirect("accounts:login")
