from django.db import models

class Login(models.Model):
    firstName = models.CharField(max_length = 64)
    lastName = models.CharField(max_length = 64)
    comment = models.CharField(max_length = 250)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.firstName} & {self.lastName} - {self.comment} - {self.duration}"
