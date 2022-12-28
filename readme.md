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



## 📍 Description
1. accounts 앱 개발

   1. 회원가입/로그인/회원정보 수정/회원탈퇴
   2. 핸드폰 문자 인증
      1. 네이버 클라우드 플랫폼을 이용해 사용자가 입력한 핸드폰 번호로 SMS 인증 번호 전송
      2. 사용자가 받은 인증 번호를 입력하고 인증하기 버튼을 누르면 발송한 인증번호와 입력한 인증번호가 동일한지 검증 후 인증 완료
   3. 소셜 로그인
      1. 구글/카카오/네이버 계정으로 회원가입 없이 로그인 가능
   4. 반려동물 등록
      1. 회원가입 및 로그인 후 마이페이지에서 반려동물 등록 가능
      2. 여러 마리 등록 가능
      3. 이름, 나이, 성별, 중성화 여부 등 선택 가능
   5. 회원간 팔로우/차단
      1. 나를 제외한 다른 회원을 팔로우 하거나 차단 할 수 있음

2. journal 앱 개발

   1. 회원이 등록한 반려동물에 대해 일기 작성
   2. 일기를 작성할 때 반려동물 선택 가능
   3. 일기 목록 분리
   4. 목록은 언제 작성했는지, 어떤 아이에 대한 일기인지 한 눈에 보이게 함

3. AWS Elastic Beanstalk 배포

   1. S3 버킷을 사용해 업로드 되는 파일 저장
   2. RDS와 PostgreSQL을 이용해 데이터 저장

## 🔥 Issues

<details>
  <summary>[accounts 이슈] missing ), unterminated subpattern at position 3</summary>
  <div markdown="1">
    <br>❌ 에러 사항<br>
    회원가입을 시도하면 ‘missing ), unterminated subpattern at position 3' 에러 발생<br><br>
  </div>
  <div markdown="1"> 
    💡 해결 방법<br>
		accounts/models.py에 User 모델을 작성할 때 닫히지 않은 괄호가 있었음.<br>
    괄호를 추가하고 다시 회원가입을 시도하니 정상적으로 가입 됨
  </div>
</details>

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
