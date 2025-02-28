from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.dept_name