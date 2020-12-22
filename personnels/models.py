from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Personnel(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=60)
    nickName = models.CharField(max_length=20)
    hourlyWage = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Presence(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    workDate = models.DateTimeField()
    startWorking = models.DateTimeField()
    endWorking = models.DateTimeField()

    def __str__(self):
        return self.workDate
