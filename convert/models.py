from django.db import models
CONVERT_STATUS_CHOICES = (
    ("start", 'start'),
    ("failed", 'failed'),
    ('completed','completed')
)


class Convert(models.Model):
    user = models.CharField(max_length=50)
    file = models.ImageField(upload_to='original/')
    removed = models.ImageField(upload_to='removed/')
    project =  models.CharField(max_length=50,null=True,blank=True)
    status =  models.CharField(choices=CONVERT_STATUS_CHOICES,blank=True,null=True,max_length=30)
    file_name = models.CharField(null=True,blank=True,max_length=1000)

    def __str__(self):
        return str(self.file_name)

    def delete(self, using=None, keep_parents=False):
        try:
            self.file.storage.delete(self.file.name)
            self.removed.storage.delete(self.file_name)
        except:
            pass

        super().delete()
