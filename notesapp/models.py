from django.db import models
from User.models import User


# Create your models here.
class Notes(models.Model):
    TAGS = (
        ("work", "WORK"),
        ("recipes", "RECIPES"),
        ("sports", "SPORTS"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=50, choices=TAGS)

    def __str__(self):
        return self.title
