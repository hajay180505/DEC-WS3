from django.db import models

# Create your models here.
class StageEvent(models.Model):
    name = models.CharField( max_length=25)
    detail = models.CharField( max_length=25)
    organizer = models.CharField( max_length=25)

class StageEventShow(models.Model):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    stage_event = models.ForeignKey(StageEvent, on_delete=models.CASCADE)

class TicketBooking(models.Model):
   price = models.FloatField()
   customer = models.CharField(max_length=45)
   no_of_seats = models.FloatField()
   stage_event_show = models.ForeignKey(StageEventShow, on_delete=models.CASCADE)

