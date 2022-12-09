from django.db import models
from django_quill.fields import QuillField


class Openings(models.Model):
    job_title = models.CharField(max_length=128, null=False, blank=False)
    hiring_city = models.CharField(max_length=128, null=False, blank=False)
    hiring_state = models.CharField(max_length=128, null=False, blank=False)
    hiring_country = models.CharField(max_length=128, null=False, blank=False)
    zip_code = models.CharField(max_length=128, null=False, blank=False)
    salary_range_from = models.IntegerField(null=False, blank=False)
    salary_range_to = models.IntegerField(null=False, blank=False)
    job_role = models.CharField(max_length=128, null=False, blank=False)
    domain = models.CharField(max_length=128, null=False, blank=False)
    job_description = QuillField()
    experience_from_years = models.SmallIntegerField(null=False, blank=False)
    experience_to_years = models.SmallIntegerField(null=False, blank=False)
    permanent = models.BooleanField(default=True)
    posted_date = models.DateField(null=False, blank=False, auto_now_add=True)
    online = models.BooleanField(default=True)
    full_time_job = models.BooleanField(default=True)
    job_country = models.CharField(max_length=128, null=False, blank=False)
    industries = models.CharField(max_length=128, null=False, blank=False)
    job_description_file = models.FileField(upload_to='JD/')
    display = models.BooleanField(default=True)
    objects = models.manager

    def __str__(self):
        return self.job_title
