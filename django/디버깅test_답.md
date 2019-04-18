> settings.py

```python
USE_TZ = True

INSTALLED_APPS = [
'accounts',
]

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'practice', 'templates')],}
```

> accounts/urls.py

```python
urlpatterns 
```



1.  migrate

* `django.core.exceptions.ImproperlyConfigured: Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited; form CommentForm needs updating.`

>  boards/forms.py

```python3
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        
```

field -> fields



2. 

```
TemplateSyntaxError at /boards/create/
Invalid block tag on line 10: 'bootstrap_form', expected 'endblock'. Did you forget to register or load this tag?
```

> boards/form.html

```python
{% load bootstrap4 %}
```



3. ```
   BootstrapError at /boards/create/
   Parameter "form" should contain a valid Django Form.
   ```

``` html
  {% bootstrap_form form %} 
  -> {% bootstrap_form board_form %}
```



4. ```
   NameError at /boards/create/
   name 'redirect' is not defined
   ```

```python
from django.shortcuts import redirect
```



5. ```
   TypeError at /boards/2/
   detail() got an unexpected keyword argument 'pk'
   Request Method:	GET
   ```

```python
path('<int:pk>/', views.detail, name='detail'),
-> path('<int:board_pk>/', views.detail, name='detail'),
```



6. ```
   IntegrityError at /boards/2/comments/create/
   NOT NULL constraint failed: boards_comment.user_id
   ```

```python
def comment_create(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
       comment_form.save()
    return redirect('boards:detail', board_pk)
->
def comment_create(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.board=board
        comment.save()
    return redirect('boards:detail', board_pk)
```



7. Edit 

````
BootstrapError at /boards/2/update/
Parameter "form" should contain a valid Django Form.
````

```
/home/ubuntu/workspace/django/debuggingtest-master/boards/views.py in edit
    return render(request, 'boards/form.html', ctx) 
```

```python
# views.py def edit
ctx = {
        'form': board_update_form,
    }
-> 
ctx = {
        'board_form': board_update_form,
    }
```

```html
# fors.html
{% bootstrap_form board_form %}
```



8. logout

```python
def logout(request):
    auth_logout(request)
    return redirect('boards:list')
```

