# 230118 목
## 게시판 만들기 - 1

1. Question 클래스 정의
 - 게시글에 있어야 할 항목을 정하자
    1. 내용이 있을테고(content)
    2. 작성자가 있을테고(user)
```
polls/models.py

class Question(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

accounts/models.py
class User(AbstractUser):
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')

```
 - Question이라는 클래스에 title, user 컬럼을 만든다.
 - user를 ForeignKey(settings.AUTH_USER_MODEL)로 세팅한 이유? 
    1. 우선, accounts/models.py에서 User class를 정의하였고 이 클래스는 AbstractUser 클래스를 상속받았다.
    2. 마스터앱(recap) settings.py에서 `AUTH_USER_MODEL = 'accounts.User`을 설정하였다.
    - 설정한 이유는? -> Question 클래스에서 ForeignKey를 설정하지 않으면 기본적으로 내장되어 있는 AUTH_USER_MODEL을 사용하겠다라는 의미인데 나는, 그러지 않을 것이고 내가 따로 정의한 User클래스를 사용하겠다의 의미로 설정해준 것이다.
---


2. Reply 클래스 정의
 - 답글(댓글)에 있어야 할 컬럼 세팅하자
   1. 답글내용이 있을테고(content)
   2. 답글에 좋아요한 사람이 있을테고(vote_users)
   3. 답글을 단 게시글이 있을테고(question)
   4. 답글을 단 사용자가 있을테고(user)

```
class Reply(models.Model):
    content = models.CharField(max_length=200)
    # reply.___.all() -> 이 reply와 m:n 관계를 가지고 있는 User들이 나와야한다.
    vote_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        # user._____.all() -> 이 User와 M:N Reply가 나와야한다.
        related_name='vote_replies'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
```

- 어느 게시글에 답글을 달았는지가 필요하니까 `question`컬럼을 ForeignKey로 받아온 것이고
- 누가 답글을 달았는지 필요하니까 `user`컬럼을 ForeignKey로 받아온 것이고
- 어느 댓글에 누가 좋아요를 눌렀는지 필요하니까 `vote_users`를 ManyToManyField로 세팅한 것이다.
    1. `Question`테이블과 `Reply`테이블 사이 중개테이블(좋아요 테이블)의 역할을 하는 것 -> vote_users 




 