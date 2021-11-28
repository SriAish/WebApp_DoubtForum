from django.db import models
from django.conf import settings


class Subject(models.Model):
    """
    Stores a single subject.
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Doubt(models.Model):
    """
    Stores a single doubt, related
    to :model:`DoubtForum.Subject`.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=160)
    body = models.TextField()
    link = models.URLField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """
    Stores a single comment, related
    to :model:`DoubtForum.Doubt`.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    doubt = models.ForeignKey('Doubt', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.doubt)


class DoubtSession(models.Model):
    """
    Stores a single doubt session, related
    to :model:`DoubtForum.Subject`.
    """
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    body = models.TextField()
    scheduled_for = models.DateTimeField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    link_to_session = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.subject.name)
