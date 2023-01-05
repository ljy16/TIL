# Django
extensions에 django설치
emmet 설치하는 이유? -> 에디터에서 확장프로그램 쓰려고!
vscode => ctrl + , => emmet 검색 => emmet : Include Languages => django-html | html 추가

1. 최상단 폴더 안에서 새로운 폴더 생성 (mkdir dirname) ex) 03_DJANGO -> mkdir TEMPLATE_VIEW

2. (vscode는 생성 폴더가 최상단으로 오도록)  장고 설치 (pip install django==3.2.16)  
   
3. 프로젝트 생성 (django-admin startproject 'template_view') 
    - 일반적으로 폴더명과 동일한 프로젝트명으로 생성함(구분하기 위해 소문자)
    - 프로젝트를 생성하면 manage.py도 같이 생성됨.
    - 최상단 폴더와 동일한 폴더 -> 마스터 앱이라 부름(template_view -> MASTER APP)
  
4. 실무는 app이 할거니까 app 생성해야함.
    - 앱 생성코드 -> python manage.py startapp <app name>

5. 앱 생성했으면 master app settings에서 installed_apps에 앱 등록해야함.

6. 마스터 url에서 include하고 path경로 설정해줘야함
    - path('review/', include('reviews.urls')),
    - review라고 치면 뒤에껀 볼 필요 없이 reviews.urls로 넘긴다는 뜻
  
7. review앱에서 urls.py생성
   - -> from django.urls import path 코드 입력 urlpatterns 입력하고
  
8. views.py로 가서 함수 입력, 이때 함수명은 입력할 값과 동일하게 세팅(ex index)

9. urls.py에서 views.py에 있는 index 함수경로확인이 안되니까 urls.py에 from . import views 입력해야함.

10. views.py에 있는 index 함수의 최종값은 기승전 return render()이어야 하고 렌더 함수는 1. reqeust | 2. html 이름 | 3. 넘길 데이터)를 필요로함.

11. render함수는 html을 필요로 하니까 html만들어야 하는데 html은 templates폴더에서 만들어야 하므로 review폴더 안에 templates폴더 만들고 그 폴더 안에 index.html 생성

12. 나타낼 값 h1 index(이건 대충해도됨) 보이게 하고
다시 index함수 돌아와서 'index.html' 입력하고 서버 돌린다음 주소창에 review/ index입력하면 최종 index(두껍게)가 나옴.

13. 하지만 review/templates에 있는 html에 있는 내용이 너무 중복되는것이 문제
    - -> html 공용 템플릿을 만들자!
    - -> 마스터 앱 바로 바깥에 templates 폴더 생성
    - -> master app settings에서 templates->dirs-> BASE_DIR / 'templates' 입력
  
14. templates폴더에 base.html 생성
    - body에 {% block content %}{% endblock content %} 입력
    - review/templates/index.html에서 내가 공용 템플릿을 쓰겠다 하는 코드가
    - `{% include 'base.html' %}` 이고 `{% block content %} {% endblock content %}` 사이에 내용 입력하면 됨

15. 