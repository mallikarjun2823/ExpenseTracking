from django.db import models

class Session(models.Model):
    pid = models.AutoField(primary_key= True)
    req_type = models.CharField(max_length= 10)

    def __str__(self):
        return f"Session {self.pid} - {self.req_type}"
# Create your models here.
