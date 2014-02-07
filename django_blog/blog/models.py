# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxLengthValidator


class Category(models.Model):
    category = models.CharField(
        u'Categorias', primary_key=True, max_length=255
    )

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __unicode__(self):
        return self.category


class Posts(models.Model):
    owner = models.ForeignKey(
        User, related_name='entries', verbose_name='Criador')
    title = models.CharField(u'Título', max_length=100)
    resumo = models.TextField(u'Resumo', validators=[MaxLengthValidator(220)])
    wording = models.TextField(u'Texto')
    tags = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(
        u'Data de Publicação', auto_now_add=True)
    published = models.BooleanField(u'Publicar?', default=False)

    class Meta:
        verbose_name = u'Postagem'
        verbose_name_plural = u'Postagens'

    def __unicode__(self):
        return self.title
