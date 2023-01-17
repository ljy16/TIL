# 230117 수 
## 프로젝트 : 게시판 CRUD
 - models.py에서 db 세팅
 - 여기서 중요한 것 : 내가 어떤 기능을 웹에서 보여주고 싶은지가 완료되어야 db세팅하는 것이 수월하고 이후 과정에서 스무스하게 진행될 수 있음

```
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, realted_name = 'comments')
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(autho_now=True)
```

- 유저가 작성한 `Article`과 그 article에 달린 `Comment`는 1 : N 의 관계임
```
Article : Comment = 1 : N
```

- 1 : N 의 관계에서 N이 정보를 더 많이 가지고 있다.
- Comment에서 article의 정보를 가지고 있고, Comment가 N이다 -> `ForeignKey`는 N테이블에서 작성해야한다.
---
```
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    def __str__(self):
        return f'{self.pk} : {self.name}'



class Feed(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='feeds')
    content = models.TextField()
    like_people = models.ManyToManyField(Person, related_name='like_feeds') # 컬럼을 추가하는 것이 아니라 테이블을 만드는것임.


class Comment(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
```

1:N에서 1입장에서 N들을 불러올 때 Reverse Manager가 자동으로 설정된다.
1. **Feed모델에 author만 있었을때**

- Person(1) : Feed(N)관계로 Person테이블에 연결된 N테이블 항목들이라는 의미로 xxx_set 리버스 매니저가 디폴트로 제공되었다.
- 그래서 `p1.feed_set`은  p1이 feed를 부를때 쓰는 리버스 매니저를 의미한다. 
- 이 매니저의 여러 메소드를 통해 p1에서 feed에 접근 가능했다.
- Feed모델에 author만 정의돼 있었을때는 `p1.feed_set.all()`이 p1이 쓴 모든 feed을 의미했다.
---
2. **Feed모델에 like_feeds를 추가할 때 migration 오류가 나서 DB생성 안 됨.**
- Why?
- People(M) : Feed(N) 관계가 하나 더 생겼다. 
- Person과 N관계가 두개가 생긴 Feed입장에서는 xxx_set 리버스 매니저가 어디에도 자동 배정될 수 없기 때문이다.
---
3. **그래서 Feed모델의 author에 리버스매니저의 related_name을 따로 지어주었더니  like_feeds를 추가해도 migration 오류 없이 DB가 생성됐다.**
- `author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='feeds')`
- like_feeds은 related_name을 따로 지정해주지 않은 경우
- `like_people = models.ManyToManyField(Person)`
- `p1.feed_set.all()` 리버스매니저는 이제 p1이 쓴 모든 글이 아닌, p1이 좋아요 한 글을 의미한다.
---
4. **like_feeds의 related_name을 'like_feeds'로 바꿔줌**
- `like_people = models.ManyToManyField(Person, related_name='like_feeds')`
- `p1.feed_set` 은 이제 없다.
- p1으로 Feed모델에 접근 가능하게 하는 리버스매니저 `p1.feeds`
- p1으로 (ManyToManyField로 자동생성된)좋아요 join테이블에 접근 가능하게 하는 리버스 매니저  `p1.like_feeds`만 있다. 