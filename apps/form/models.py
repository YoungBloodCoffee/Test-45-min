from __future__ import unicode_literals

from django.db import models


class Form(models.Model):
	secret = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Likes(models.Model):
	like_count = models.IntegerField()
	secret = ForeignKey(Form)
	updated_at = models.DateTimeField(auto_now = True)
