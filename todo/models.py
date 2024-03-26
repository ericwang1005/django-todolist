from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    date_comleted = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)

    # user => user.id | user_id 會綁定 todo_id
    # on_delete=models.CASCADE , CASCADE => 是當User(主人)消失就會連同TODO的資料一起消失
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)
    # 更改後端ADMIN的資料名稱

    def __str__(self) -> str:
        return f'{self.id}-{self.title}'
