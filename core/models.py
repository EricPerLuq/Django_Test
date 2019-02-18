from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
# Create your models here.
class Projecte(models.Model):
	nom= models.CharField(max_length=200,help_text="Nom del Projecte")
	descripcio= models.TextField(blank=True, null=True)
	scrum_master=models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="Scrum_Master",
		)
	Product_Owner=models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="Product_Owner",
		)
	Grup =models.ForeignKey(Group,
		on_delete=models.CASCADE)
	def __str__(self):
		return self.nom
class Sprint(models.Model):
	Projecte= models.ForeignKey(
		Projecte,
		on_delete=models.CASCADE)
	data_inici=models.DateField()
	data_final=models.DateField()
	hores=models.IntegerField(default=0,help_text="bla-bla")

class Spec(models.Model):
	DIFICULTAT=(
		("D","DESCONEGUDA"),
		("B","BAIXA"),
		("M","MITJANA"),
		("A","ALTA"),

		)
	descripcio=models.TextField()
	dificultat=models.CharField(max_length=1,choices=DIFICULTAT,default="D")
	hores=models.IntegerField(default=0)
	Projecte=models.ForeignKey(Projecte,
		on_delete=models.CASCADE)
	Sprint=models.ForeignKey(Sprint,
		on_delete=models.CASCADE,null=True,blank=True)
	developer=models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,null=True,blank=True)
	def __str__(self):
		return self.descripcio




















