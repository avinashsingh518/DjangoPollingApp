from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option

class Register(models.Model):
    emailid = models.EmailField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=50)



    def __str__(self):
        return self.username
