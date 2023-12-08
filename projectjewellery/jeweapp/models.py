from django.db import models

class pmodel(models.Model):
	iname = models.CharField(max_length=50)
	cname = models.CharField(max_length=20)
	scname = models.CharField(max_length=20)
	modal = models.CharField(max_length=100)
	wght = models.CharField(max_length=20)
	stonedtl = models.CharField(max_length=200)
	swght = models.CharField(max_length=20)
	sprice = models.CharField(max_length=20)
	mcharge = models.CharField(max_length=20)
	size = models.CharField(max_length=100)
	descp = models.CharField(max_length=300)
	qty = models.CharField(max_length=20)
	p_image= models.FileField(upload_to='pictures')
	class Meta:
		db_table = "item"