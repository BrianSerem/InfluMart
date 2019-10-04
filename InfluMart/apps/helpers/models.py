from django.db import models

class BaseAbstractModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = False)

    def soft_delete(self):

        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
        ordering = ['-created_at']



