from django.db import models

# Create your models here.
class Host(models.Model):
    name        = models.CharField(max_length=50)
    ipaddress   = models.CharField(max_length=20)
    username    = models.CharField(max_length=50)
    password    = models.CharField(max_length=20)
    ssh_port    = models.IntegerField()
    hostname    = models.CharField(max_length=45, blank=True)
    cpu         = models.CharField(max_length=45, blank=True)
    memory      = models.CharField(max_length=45, blank=True)
    disk        = models.CharField(max_length=45, blank=True)
    system      = models.CharField(max_length=45, blank=True)
    application = models.CharField(max_length=100, blank=True)
    status      = models.CharField(max_length=20, blank=True)
    remark      = models.TextField(max_length=100, blank=True)


class HostMetric(models.Model):
    host         = models.ForeignKey(Host)
    cpu_load     = models.CharField(max_length=45)
    disk_usage   = models.CharField(max_length=45)
    memory_usage = models.CharField(max_length=45)
    datetime     = models.DateTimeField()

class Oracle(models.Model):
    host          = models.ForeignKey(Host)
    db_user       = models.CharField(max_length=50)
    db_password   = models.CharField(max_length=20)
    db_port       = models.IntegerField(max_length=8)
    db_id         = models.CharField(max_length=20, blank=True)
    db_name       = models.CharField(max_length=30, blank=True)
    db_version    = models.CharField(max_length=20, blank=True)
    service_name  = models.CharField(max_length=20, blank=True)
    remark        = models.TextField(max_length=100, blank=True)
#
# class OracleMetric(models.Model):
#     oracle     = models.ForeignKey(Oracle)
#     db_session = models.IntegerField()
#     db_lock    = models.CharField(max_length=10)
