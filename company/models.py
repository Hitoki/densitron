"""Module Company models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.db import models


class People(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    description = models.TextField()
    photo = models.ImageField(
        upload_to='images', null=True, blank=True,
        help_text=
        'Best size: 396px/296px. Min-width: 396px, Min-height: 296px.')
    place_priority = models.SmallIntegerField(
        default=1,
        help_text='Display priority list. 1 - top, 2+ - bottom. (max 32767)')
    team = models.ForeignKey('Team')
    job = models.ForeignKey('Job')

    class Meta:
        ordering = ['job__place_priority', 'place_priority']
        verbose_name_plural = 'People'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    place_priority = models.SmallIntegerField(
        default=1,
        help_text='Display priority list. 1 - top, 2+ - bottom. (max 32767)')

    class Meta:
        ordering = ['place_priority']

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    place_priority = models.SmallIntegerField(
        default=1,
        help_text='Display priority list. 1 - top, 2+ - bottom. (max 32767)')

    class Meta:
        ordering = ['place_priority']

    def __str__(self):
        return self.name


class Admin(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    get_emails = models.BooleanField(default=True)

    def __str__(self):
        return '{}{}'.format(self.first_name, self.last_name)


class ContactUser(models.Model):
    first_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    job = models.CharField(max_length=128)

    class Meta:
        ordering = ['surname']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.surname)


class Address(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title = models.CharField(max_length=128)
    line_1 = models.CharField(max_length=128)
    line_2 = models.CharField(max_length=128)

    phone = models.CharField(max_length=36)
    email = models.EmailField(max_length=128, blank=True, null=True)

    lat = models.DecimalField(max_digits=10, decimal_places=7,
                              blank=True, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=7,
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Addresses'


class Opportunity(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Opportunities'