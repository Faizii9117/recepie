from django.db import models

# Create your models here.

class vegi(models.Model):
    recepie_name = models.CharField(max_length=100)
    recepie_desc = models.TextField()
    recepie_image = models.ImageField(upload_to="recepies/", null=True, blank=True)


class login_api(models.Model):
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)


    def __str__(self):
        return self.username
    

# class register(models.Model):
#      username = models.CharField(max_length=100)
#      password = models.CharField(max_length=100)






