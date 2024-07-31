from django.db import models

from django.urls import reverse # used in get_absolute_url() to get URL for Scecified ID
from django.db.models import UniqueConstraint # Constrains Fields to unique values
from django.db.models.functions import Lower # Returns Lower cased value of field

# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        help_text='Enter a book genre (e.g. Science Fiction)',
        unique=True,
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this genre."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique'
                violation_message='Genre with this name already exists. (case insensitive match)'
            )
        ]