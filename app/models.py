from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from .utils import get_random_number


class User(AbstractUser):
    birthday = models.DateField()
    random_number = models.IntegerField(default=get_random_number)

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.id])

    @property
    def age(self):
        today = timezone.now().date()
        if self.birthday:
            return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

        return 0
