from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class person(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField()
    age = models.IntegerField()
    profile_pic = models.ImageField(upload_to='person/%Y/%m/%d',null = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

class bookIssue(models.Model):
    student = models.ForeignKey(person, on_delete= models.CASCADE,related_name='issues')
    book_name = models.CharField(max_length= 200)
    cover = models.FileField(upload_to='book_covers/%Y/%m/%d',null = True)
    author = models.CharField(max_length= 200)
    Issued_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.book_name

class signupModel(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    date_of_birth = models.DateField()
    pic = models.ImageField(upload_to='user/%Y/%m/%d')
    registered_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username
