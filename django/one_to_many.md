(git bash로)프로젝트 생성하면 일단 touch README.md .gitignore 하고 세팅하는걸 습관화하자!
-> 바로 python -m venv venv
code .로 들어감

터미널에서 venv키는법 -> ctrl+shift+p -> select interpreter에서 venv선택
gitignore.io에서 venv/django/python 생성해서 해당 코드 gitignore에 붙여넣기해야함.(이건 프로젝트 생성때마다) -> 안하면 커밋에 몇천개떠있음.
터미널에서 pip install django==3.2.16하고 pip freeze > requirements.txt 생성
아이콘 조금더 직관적으로 보여주기 -> extensions에서 vscode-icons설치(선택사항.)
프로젝트 생성 -> django-admin startproject one_to_many .

앱 생성 ->python manage.py startapp board

쭉쭉 생성하면 되는데 board안에 
mkdir -p templats/board로 하는게 편함.
앱 안에서 touch urls.py forms.py 하고

models에서 디비 세팅
-> 디비세팅끝났으면
python manage.py makemigrations board (<app_name>)
python manage.py migrate board

하고 python install django extensions하고 settings에서 installed_apps에서 'django_extensions' 등록해야함.

forms.py로 이동