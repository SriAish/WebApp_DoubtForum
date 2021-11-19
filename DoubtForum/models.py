from django.db import models 
    

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Doubt(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=10, unique=True)
    body = models.TextField()
    link = models.CharField(max_length=50 ,null =True)
    created_on = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='doubts')

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    doubt = models.ForeignKey('Doubt', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.doubt)