from django.db import models
from datetime import datetime


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()  # see docs! class EmptyManager??

    class Meta:
        abstract = True

    def delete(self, hard=False):
        if hard:
            super(SoftDeleteModel, self).delete()
        else:
            self.deleted_at = datetime.now()
            self.save()

    def restore(self):
      self.deleted_at = None  # None == Null in the DB?
      self.save()
