from django.db import models

class Thing(models.Model):
    name             = models.CharField(unique=True, max_length=255)
    slug             = models.SlugField(unique=True, max_length=255)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('thing_detail', (), {'thing_slug': self.slug})
