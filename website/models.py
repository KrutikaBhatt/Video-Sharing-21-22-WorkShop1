from django.db import models
from django.db.models.fields import CharField, TextField
from datetime import date

# Create your models here.


class User(models.Model):

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    emailID = models.EmailField(unique=True)
    pfp = models.ImageField()



    def __str__(self):
        return self.username


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = TextField(max_length=1000)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField
    date =  date.today()
    #thumbnail= models.ImageField()

    def __str__(self):
        return self.user.username + ' : ' + self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Video =models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)

    def str(self):
        return self.user.username

    def __str__(self):
        return self.user.username + ' : ' + self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.user.username
