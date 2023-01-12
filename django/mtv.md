다른사람과  협업할때 가상머신을 사용하는 것이 적절하다.
-> 진행중인 프로젝트에서 어떤 패키지를 설치해야 제대로 작동되는지 본인조차 알 수 없는 경우가 많은데 이 경우를 대신하는 것이 가상머신 사용하는 것
-> 새로운 프로젝트에서 각각의 파이썬 패키지를 설치한다.(글로벌에서 안가져옴)
프로젝트 경로로 들어가서 'python -m venv <env name> 명령어 입력(이번 프로젝트에서는 env name = venv 동일하게 했음)
source venv/Scripts/activate -> 글로벌이 아니고 내부에서 파이썬 패키지를 사용하겠다 라는 의미
deactivate하면 다시 글로벌을 사용하겠다
5.1 MTV폴더 안에서 다시 장고를 설치하겠다 -> pip install django==3.2.16
장고설치완료된거고 여기서 프로젝트 생성 -> django-admin startproject mtv .
code . -> vscode 바로열어줌
커밋에 6천개 이상있음 -> gitignore.io가서 python / django / venv생성 누르고 전체 복사해서 venv에 있는 gitignore에 붙여넣기 저장하면 됨


세팅쭉완료하고 blog/models.py에서 
```
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # 생성시 자동으로 채워지도록 -> DateTimeField만 가능
    created_at = models.DateTimeField(auto_now_add=True)

    # 생성/수정시 자동으로 채워지도록 -> DateTimeField만 가능
    updated_at = models.DateTimeField(auto_now=True)
```
작성하고 명령어로
 `python manage.py makemigrations blog` 
`python manage.py migrate blog`

작성하면 디비에 blog_article로 생성됨(이때, db에 id는 자동생성됨)

장고 관리자 계정 만들기
python manage.py createsuperuser

admin.py가서 

post방식 -> db에 변경이 일어날때 사용
그 외엔 get방식으로 사용