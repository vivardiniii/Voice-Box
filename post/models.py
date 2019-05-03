from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
HASHTAG_CHOICES = (

    ('art', 'art'),
    ('food', 'food'),
    ('tech', 'tech'),
    ('mood', 'mood'),
    ('fashion', 'fashion'),
    ('wildlife', 'wildlife')
)

class Post(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    hname = MultiSelectField(choices = HASHTAG_CHOICES)

    def __str__(self):
        return self.title


class Hashtag(models.Model):

    hashname = models.ManyToManyField(Post)

    def __str__(self):
        return self.hashname
