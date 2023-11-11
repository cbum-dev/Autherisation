from django.db import models


class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100,null=False)
    model = models.CharField(max_length=100,null=False)
    year = models.IntegerField(default=1900)
    created_at = models.DateTimeField(auto_now_add=True)
    