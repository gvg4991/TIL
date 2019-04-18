## TemplateSyntaxError

템플릿 안의 html의 중괄호 문제

```html
{% load bootstrap4 %}
```





## Forbidden

{% csrf_token %} 넣어주기



## Page not found

주소와 관련된 문제(링크에 걸린 주소가 잘못되거나 주소가 없거나)

url.py 주소 확인,  href 주소(name있으면  : , name없으면 /)

```python
app_name = 'accounts'
urlpatterns = [
    path('profile/update/',views.profile_update, name='profile_update'),
    ]
```

```html
    {% if user == people %}
    <div>
        <a href="{% url 'accounts:profile_update' %}">프로필 수정</a><span> | </span>
        <a href="{% url 'accounts:update' %}">계정 정보 수정</a>
    </div>
    {% endif %}
    <div class="row">
        {% for post in people.post_set.all %}
        <div class='col-4'>
            <img src="{{ post.image_set.first.file.url }}" class="img-fluid"/> <!--포스트의 첫번째 사진-->
        </div>
        {% endfor %}
    </div>
</div>
```





## NameError at /주소/

at 뒤에 주소나오면 파이썬 문제 -> views.py확인

- not define: 변수명 에러 

```python
def people(request, username):
    people = get_object_or_404(get_user_model(), username=user)
    # user라는 변수명이 없음! username으로 수정
    return render(request, 'accounts/people.html', {'people':people})
```





## IntegrityError

Not Null constraint failed: posts_comment.post_id : post_id 값이 없음



## http Error 405

post방식으로 들어와야 하는 곳에 get 방식으로 들어옴.

form태그에 method="POST"를 넣어야됨

```html
  <form action="{% url 'posts:comment_create' post.id %}" method = "POST">
    {% csrf_token %}
    <div class="input-group">
      {{ comment_form }}
      <div class="input-group-prepend">
        <input type="submit" value="Submit" class='btn btn-info'/>
      </div>
    </div>
  </form>
```





## NoReverseMatch at /posts/

Reverse for 'comment' not found. 'comment' is not a valid view function or pattern name

urls.py의 name 부분에 comment가 있는지 확인

comment 이름을 사용한 곳 확인

-> 이름이 매치가 안돼서 뜨는 error                                                                                                                                                     





## unknown field(s) (title)

forms.py 의 필드에 없는 값을 써서 발생

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','introduction','image',]
```



## OperationalError at [url]

no such column: movies_score.movie_id

```python
./manage.py makemigrations
./manage.py migrate
```





## contents 내용 안들어감

models.py의 class 중 컨텐츠 하나를 입력 안할 때

1.  default = '123' 값을 넣어주거나 blank = True 입력
2. 그냥 무시하고 마이그레이트 안함

```python
class Post(models.Model):
    title = models.TextField(blank=True)
    content = models.TextField(default='123')
```

ex) 어떤 사람이 댓글을 썼는데 제목만 값이 들어가있음 이를 작성자명과 함께 뜨도록 등록하세요.



## list창에 뜨는게 없음

block의 이름이 다름

```html
base.html
	{% block container %}
    {% endblock %}

html
	{% block body %}
    	<h1></h1>
	{% endblock %}
```



## settings.py

```python
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True #머하는 칭군지? 랭귀지코드 사용을 트루

USE_L10N = True #몰라도됨

USE_TZ = True #머하는 칭군지? 타임존 사용을 트루
```

settings에서 107 (ko-kr), 109 (Asia/Seoul), 33마지막에 ((pages).apps.(Pages)Config) 추가    -()에 앱이름 넣기