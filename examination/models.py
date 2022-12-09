from django_quill.fields import QuillField
from django.db import models


class LRExam(models.Model):
    question = QuillField()
    option1 = models.CharField(max_length=128, null=False, blank=False)
    option2 = models.CharField(max_length=128, null=False, blank=False)
    option3 = models.CharField(max_length=128, null=False, blank=False)
    option4 = models.CharField(max_length=128, null=False, blank=False)
    answer = models.CharField(max_length=128, null=False, blank=False)
    objects = models.manager

    def __str__(self):
        return self.question


class Paragraph(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    paragraph = models.TextField(null=False, blank=False)
    objects = models.manager

    def __str__(self):
        return self.title


class EnglishExam(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    question = QuillField()
    option1 = models.CharField(max_length=64, null=False, blank=False)
    option2 = models.CharField(max_length=64, null=False, blank=False)
    option3 = models.CharField(max_length=64, null=False, blank=False)
    option4 = models.CharField(max_length=64, null=False, blank=False)
    answer = models.CharField(max_length=64, null=False, blank=False)
    objects = models.manager

    def __str__(self):
        return self.question


class ComputerExam(models.Model):
    question = QuillField()
    option1 = models.CharField(max_length=128, null=False, blank=False)
    option2 = models.CharField(max_length=128, null=False, blank=False)
    option3 = models.CharField(max_length=128, null=False, blank=False)
    option4 = models.CharField(max_length=128, null=False, blank=False)
    answer = models.CharField(max_length=64, null=False, blank=False)
    objects = models.manager

    def __str__(self):
        return self.question
