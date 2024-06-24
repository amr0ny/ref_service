from django.db import models
import uuid

class Ref(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255)
    class Meta:
        db_table = 'ref'
    
    def __str__(self):
        return self.url

class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    ref_index = models.IntegerField(default=0)
    refs = models.ManyToManyField(Ref, through='LinkRef')

    class Meta:
        db_table = 'link'
    
    def __str__(self):
        return self.name


class LinkRef(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ref = models.ForeignKey(Ref, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    class Meta:
        db_table = 'link_ref'

class LinkAccess(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_address = models.GenericIPAddressField()
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    ref_index = models.IntegerField()
    access_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'link_access'
        indexes = [
            models.Index(fields=['ip_address']),
            models.Index(fields=['link']),
        ]