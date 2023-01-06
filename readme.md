# 🗂 Final Project

> 서비스 이름 : 당신 근처의 집사, 당근집사🐾
>
> 프로젝트 기간 : 2022-11-24 ~ 2022-12-14
>
> 팀원 : 윤혜진, 이상백, 이정섭, 한가을, 황여원
>
> 🌐 Link : http://danggeunjibsa-env.eba-y8yce3qe.ap-northeast-2.elasticbeanstalk.com/



## 🏆 award

<img src="readme.assets/IMG_0141-1196370.jpg" alt="IMG_0141" style="zoom:50%;" />



## 🫧 Preview

- 커뮤니티

<img src="readme.assets/community-1-1171759.gif" alt="community-1" style="zoom:50%;" />

- 산책메이트

<img src="readme.assets/dogwalking-1.gif" alt="dogwalking-1" style="zoom:50%;" />

- 돌봄

<img src="readme.assets/care-1.gif" alt="care-1" style="zoom:50%;" />

- 지도

<img src="readme.assets/information-1.gif" alt="information-1" style="zoom:50%;" />



## 📈 purpose

1. 반려동물에 관한 정보를 서로 공유하고 소통할 수 있는 커뮤니티를 구현
2. 같은 지역, 같은 동네에 있는 반려인들끼리 모여 함께 산책하거나 돌봄 서비스를 제공할 수 있게 함
3. 지도 API를 통해 내 위치 주변에 있는 동물병원, 반려동물 동반 식당/카페, 반려동물 용품점 등을 편리하게 검색 가능
4. 프로필 페이지에서 등록한 반려동물에 대한 자유롭게 작성할 수 있는 일기 / 산책 기록을 남기는 산책일기 / 급여, 활력, 약 기록 등을 남기는 건강일기 작성 가능



## ⚙️ Stacks

- Backend

<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Python-3776AB?stype=flat-square&logo=Python&logoColor=white">

- Frontend

![img](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff) ![img](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff) ![img](https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=black) 

- DB

<img src="https://img.shields.io/badge/SQLite-003B57?stype=flat-square&logo=SQLite&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=PostgreSQL&logoColor=ffffff"/>  

- Tools

<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>  

- Delpoy

<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat-square&logo=Amazon S3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=flat-square&logo=Amazon RDS&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=flat-square&logo=GitHub Actions&logoColor=ffffff"/>


## 🔥 Issues

<details>
  <summary>[AWS 이슈] Incorrect application version found on all instances</summary>
  <div markdown="1">
    <br>❌ 에러 사항<br>
    aws 배포시 애플리케이션 버전에 다르다는 에러 메시지가 나오면서 배포 적용이 되지 않음.<br><br>
  </div>
  <div markdown="1"> 
    💡 해결 방법<br>
		`.ebextensions` 폴더 안에 `django.config` 파일 외에 다른 config 파일이 있어서 오류가 발생.<br>
    해당 config 파일은 이미지 업로드 용량을 바꾸기 위해 넣은 파일이었는데 `.platform/nginx/conf.d` 폴더에 cofn 파일 생성 후 내용을 옮기고 삭제 함.<br>
    이후 정상적으로 배포 적용됨.
  </div>
</details>

<details>
  <summary>[AWS 이슈] Server Error 500</summary>
  <div markdown="1">
    <br>❌ 에러 사항<br>
    배포 후 특정 페이지에서만 server error 500 에러가 발생.<br><br>
  </div>
  <div markdown="1"> 
    💡 해결 방법<br>
		DB 테이블이 제대로 생성되지 않아서 발생한 에러.<br>
    기존에 있던 DB를 삭제하고 처음부터 다시 DB를 생성하니 페이지 및 기능들이 정상적으로 작동 됨.
  </div>
</details>
