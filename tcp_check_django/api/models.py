from django.db import models

class Port(models.Model):
    ip_address = models.CharField(max_length=200)
    port_number = models.IntegerField()
    is_open = models.BooleanField(default=False)


    class Meta:
        unique_together = (('ip_address', 'port_number'),)

    def __str__(self):
        return f"{self.ip_address}:{self.port_number}"
