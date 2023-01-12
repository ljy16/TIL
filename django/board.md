# django project 생성 순서

## 1 . 프로젝트 생성
```
mkdir <project_name>
```

## 2. README.md , .gitignore 생성
```
touch README.md .gitignore
```
-> 먼저 생성하는 것을 습관화하자!

## 3. venv 설치
```
python -m venv <env name>
```
 - (뒤에 위치한 venv는 venv 별칭임.)
 - ctrl+shift+p 에서 select interpreter에서 venv선택

## 4. gitignore 코드 입력
 - gitignore.io에서 python / django / vevn 생성

## 5. 프로젝트 내부에서 django 및 extension 설치
```
pip install django==3.2.16 django_extensions
```
## 6. requirements.txt. 설치
```
pip freeze > requirements.txt
```

## 7. 프로젝트 생성
```
django-admin startproject <project_name>
```

## 8. app 생성
```
python manage.py startapp <app_name>
```

프로젝트 시작할때 자동적으로 해야하는 것들
 - masterapp / settings에 app 등록
 - root에서 templates생성(base.html 위치해야함.)
 - app에서 urls.py, forms.py, templates/app_name안에 필요한 html 생성
 - app / models.py에서 db 세팅하고 완료했으면

```
python manage.py makemigrations <app_name>
python manage.py migrate <app_name>
```
 - 





-> forms.py 작성
class StudentForm
-> views.py 함수 작성
-> 함수명에 요청할 html 작성

주소창에 입력해서 요청하는 것은 다 get임 