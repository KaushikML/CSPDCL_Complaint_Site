from django.db import models


class Form(models.Model):
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    bp=models.IntegerField(null=True)
    email=models.EmailField()
    date=models.DateField()
    complaint=models.CharField(max_length=80)
    explain=models.CharField(max_length=400)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
