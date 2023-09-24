from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator
class Meal(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=360)
    # id = models.UUIDField(
    #      primary_key = True,
    #      default = uuid.uuid4,
    #      editable = False)

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # id = models.UUIDField(
    #      primary_key = True,
    #      default = uuid.uuid4,
    #      editable = False)
    
    class Meta:
        unique_together = [('user','meal')]
        index_together = [('user','meal')]
    