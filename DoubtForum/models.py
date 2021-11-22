from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Doubt(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=160)
    body = models.TextField()
    link = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    subject = models.ManyToManyField('Subject', related_name='doubts')

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    doubt = models.ForeignKey('Doubt', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.doubt)


class DoubtSession(models.Model):
    professor = models.CharField(max_length=60)
    body = models.TextField()
    scheduled_for = models.DateTimeField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    link_to_session = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.subject.name)
