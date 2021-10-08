# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

from wagtail.contrib.settings.models import BaseSetting, register_setting



@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text=_('Enter Facebook URL'),
        blank=True,
        null=True
    )
    linkedin = models.URLField(
        help_text=_('Enter Linkedin URL'),
        blank=True,
        null=True
    )

    twitter = models.CharField(
        max_length=255,
        help_text=_('Enter Twitter URL'),
        blank=True,
        null=True
    )

    instagram = models.CharField(
        max_length=255,
        help_text=_('Enter Instagram username'),
        blank=True,
        null=True
    )

    api_instagram_enabled = models.BooleanField(
        default=False,
        help_text=_('Enable/Disable Instagram API'),
    )

    api_instagram_user_id = models.CharField(
        max_length=255,
        help_text=_('Enter Instagram User IDL'),
        blank=True,
        null=True
    )

    api_instagram_key = models.CharField(
        max_length=255,
        help_text=_('Enter Instagram API key'),
        blank=True,
        null=True
    )

    api_instagram_secret = models.CharField(
        max_length=255,
        help_text=_('Enter Instagram API Secret'),
        blank=True,
        null=True
    )

    youtube = models.URLField(
        help_text=_('Enter youtube URL'),
        blank=True,
        null=True
    )


@register_setting
class CompanySettings(BaseSetting):
    name = models.CharField(
        max_length=255,
        help_text=_('Company Name'),
    )

    about = models.TextField(
        max_length=1000,
        help_text=_('Write something about your company'),
        null=True,
        blank=True
    )

    logo = models.ImageField(null=True, blank=True)
    nav_logo = models.ImageField(null=True, blank=True)

    address = models.CharField(
        max_length=255,
        help_text=_('Company Address'),
        blank=True,
        null=True
    )


    zipcode = models.CharField(
        max_length=255,
        help_text=_('ZIP'),
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=255,
        help_text=_('City'),
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=255,
        help_text=_('State'),
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=255,
        help_text=_('Company Official Email'),
    )

    phone = models.CharField(
        max_length=255,
        help_text=_('Company Official Phone'),
    )