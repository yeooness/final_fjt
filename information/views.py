from django.shortcuts import render
import json

# Create your views here.
def index(request):
    name = request.GET.get("board", '동물병원')
    information_name = "모든게시판"
    information_list = ["동물병원", "애견카페", "애견식당"]
    
    # with open('static/json/animal_hospital.json', encoding='utf-8') as json_file:
    #     animal_hospitals = json.load(json_file)
    #     # ['좌표정보(x)']['좌표정보(y)']['사업장명']['소재지전체주소']['도로명전체주소']['소재지전화']['영업상태명']
    
    # animal_hospitaldict = []
    # for animal_hospital in animal_hospitals:
    #     if animal_hospital.get('mapx'):
    #         content = {
    #             "좌표정보(x)": str(animal_hospital['좌표정보(x)']),
    #             '좌표정보(y)': str(animal_hospital['좌표정보(y)']),
    #             '사업장명': animal_hospital['사업장명'],
    #             '소재지전체주소': animal_hospital['소재지전체주소'],
    #             '도로명전체주소': animal_hospital['도로명전체주소'],
    #             '소재지전화': str(animal_hospital['소재지전화']),
    #             '영업상태명': animal_hospital['영업상태명'],
    #         }
    #         animal_hospitaldict.append(content)
    #     animal_hospitalJson = json.dumps(animal_hospitaldict, ensure_ascii=False)
    #     print(animal_hospital)
    #     return render(request, 'information/index.html', {'animal_hospitalJson':animal_hospitalJson})
    context = {
        "name": name,
        "information_name": information_name,
        "information_list": information_list,
    }
    return render(request, "information/index.html",context)
    


def friends(request):

    return render(request, "information/friends.html")



