from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data["first_name"]) < 1:
            errors["first_name"] = "First name cannot be empty"
        if len(post_data["last_name"]) < 1:
            errors["last_name"] = "Last name cannot be empty"
        if len(post_data["email"]) < 1:
            errors["email"] = "Email cannot be empty"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
