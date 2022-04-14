from django.db import models
from User.models import CustomUser

# Create your models here.
class Notes(models.Model):
    TAGS = (
        ("work", "WORK"),
        ("recipes", "RECIPES"),
        ("sports", "SPORTS"),
    )
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=200)
    tags = models.CharField(max_length=50, choices=TAGS)

    def __str__(self):
        return self.title
