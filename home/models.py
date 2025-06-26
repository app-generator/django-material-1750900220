# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    failed_login_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    failed_login_count = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Question(models.Model):

    #__Question_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=255, null=True, blank=True)
    closes_on = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Question_FIELDS__END

    class Meta:
        verbose_name        = _("Question")
        verbose_name_plural = _("Question")



#__MODELS__END
