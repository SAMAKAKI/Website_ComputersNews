from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Title', max_length=150, default='Title news')
    full_text = models.TextField('Full text', default='Title text')
    date = models.DateTimeField('Date create')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
