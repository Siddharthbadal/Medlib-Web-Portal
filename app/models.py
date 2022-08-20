from django.db import models


class Patients(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=True, blank=True,)
    phone = models.CharField(max_length=20, null=True, blank=True,)
    email = models.CharField(max_length=60, null=True, blank=True,)
    age = models.CharField(max_length=60, null=True, blank=True,)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER)
    note = models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True,)

    def __str__(self) -> str:
        return self.name