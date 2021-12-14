from django.db import models

# Create your models here.

class Feedback(models.Model):
    cluster = models.CharField(max_length=25,null=True,blank=True)
    value = models.TextField()
    main_id = models.CharField(blank=True,null=True,max_length=50)
    count = models.IntegerField(default=1)
    custom = models.BooleanField(default=False)

    def __str__(self):
        return self.value
