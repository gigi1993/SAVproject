from django.db import models
from django.utils import timezone

# Create your models here.
class Click(models.Model):
    click_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=120, default='defaultIP')
    clicked = models.CharField(max_length=10, default='country')

    def __str__(self):
    	return str(self.date)