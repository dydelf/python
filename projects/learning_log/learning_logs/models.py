from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about the topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""

        #Value self.text has to be converted to str first in order to work
        if len(str(self.text))>50:
            return str(self.text)[:50] + "..."
        else:
            return str(self.text)
