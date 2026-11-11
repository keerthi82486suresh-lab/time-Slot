from django.db import models

class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    faculty_name= models.CharField(max_length=50)

    def __str__(self):
        return self.subject
