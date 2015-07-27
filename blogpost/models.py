# -*- coding: utf-8 -*- 
from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	criado_em = models.DateTimeField(
		default = timezone.now)
	publicado_em = models.DateTimeField(
		blank=True, null=True)

	def publicar(self):
		self.publicado_em = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Postêres"
